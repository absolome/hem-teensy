#!python3

import sys
from datetime import datetime

import memcard_driver
import gnc_packet
import id_db

from PyQt5.QtGui import QPainter, QColor
from pyqt5.QtWidgets import QMainWindow, QApplication
from pyqt5.QtCore import QTimer, QElapsedTimer, QRect


class Box(QMainWindow):

    """ BIG GAY DOCSTRING """
    # TODO: move calculation over to a worker thread

    refreshTimer = QTimer()
    speed = 5

    # on OS X QElapsedTimer uses MachAbsoluteTime
    debug_timer = QElapsedTimer()

    driver = memcard_driver.MemCardDriver('/dev/tty.usbserial')

    # TODO: figure out how I can not have to declare all this crap
    # probably just more classes lol
    p1x = p1y = p1percent = p1char = p1comboCount = p1stocks = p1shieldSize = p1actionState = ''
    p2x = p2y = p2percent = p2char = p2comboCount = p2stocks = p2shieldSize = p2actionState = ''
    queueSize = frameCount = ''
    prev_time = datetime.now()

    textRect = QRect(10, 10, 300, 300)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # TODO: add a close button to the main window
        # TODO: add a reset queue button to the main window
        # TODO: add a status bar to display queue info, status, and frame count
        # TODO: add a menu bar

        self.resize(500, 500)

        self.refreshTimer.setTimerType(0)

        self.refreshTimer.timeout.connect(self.onTimer)
        self.refreshTimer.start(self.speed)

        print(self.refreshTimer.timerType())

        self.show()

        self.debug_timer.start

    def onTimer(self):

        if not self.debug_timer.isValid():
            self.debug_timer.start()
        else:
            print (self.debug_timer.restart())

        # print(str((datetime.now() - self.prev_time) * 1000))
        # self.prev_time = datetime.now()

        packet = self.driver.Pop()

        # print(str(packet.player_updates[0].action_state) + ' ' + str(packet.player_updates[1].action_state))

        if packet.type == gnc_packet.PacketType.UPDATE:
            self.p1char = id_db.characters[packet.player_updates[0].char_id]
            self.p2char = id_db.characters[packet.player_updates[1].char_id]

            self.p1percent = str(packet.player_updates[0].percent)
            self.p1shieldSize = str(packet.player_updates[0].shield_size)
            self.p1stocks = str(packet.player_updates[0].stocks)
            self.p1comboCount = str(packet.player_updates[0].combo_count)

            self.p1x = str(packet.player_updates[0].xpos)
            self.p1y = str(packet.player_updates[0].ypos)
            self.p2x = str(packet.player_updates[1].xpos)
            self.p2y = str(packet.player_updates[1].ypos)

            self.p1actionState = str(packet.player_updates[
                                     0].action_state) + ' - ' + id_db.actionstates[packet.player_updates[0].action_state]
            self.p2actionState = str(packet.player_updates[
                                     1].action_state) + ' - ' + id_db.actionstates[packet.player_updates[1].action_state]

            self.queueSize = str(self.driver.queue.qsize())
            self.frameCount = str(packet.frame_count)
        else:
            self.p1x = 'Waiting for match to begin'
            self.p1y = ''
            self.p1actionState = ''
            self.p1comboCount = ''
            self.p1percent = ''
            self.p1stocks = ''
            self.p1shieldSize = ''
            self.p1char = ''
            self.frameCount = ''

        # self.update()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(qp)
        qp.end()

    def drawText(self, qp):

        # TODO: make these drawtexts less awful jesus christ

        qp.setPen(QColor(0, 0, 0))

        qp.drawText(self.textRect, 0, '----_NICE_----')

        qp.drawText(10, 70, 'Player 1 character: ' + str(self.p1char))
        qp.drawText(260, 70, 'Player 2 character: ' + str(self.p2char))
        # qp.drawText(260, 100, 'Player 1 stocks: ' + str(self.p1stocks))
        # qp.drawText(260, 130, 'Player 1 percent: ' + str(self.p1percent))
        qp.drawText(10, 160, 'Player 1 x: ' + str(self.p1x))
        qp.drawText(10, 190, 'Player 1 y: ' + str(self.p1y))
        qp.drawText(260, 160, 'Player 2 x: ' + str(self.p2x))
        qp.drawText(260, 190, 'Player 2 y: ' + str(self.p2y))
        # qp.drawText(260, 220, 'Player 1 combo counter: ' + str(self.p1comboCount))

        qp.drawText(10, 250, 'Player 1 action state: ' +
                    str(self.p1actionState))
        qp.drawText(260, 250, 'Player 2 action state: ' +
                    str(self.p2actionState))

        # qp.drawText(260, 280, 'Player 1 shield size: ' + str(self.p1shieldSize))

        qp.drawText(5, 490, 'Queued packets: ' + str(self.queueSize))
        qp.drawText(140, 490, 'Match frame count: ' + str(self.frameCount))


if __name__ == "__main__":
    app = QApplication([])
    box = Box()
    sys.exit(app.exec_())
