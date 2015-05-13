__author__ = 'Michael Redmond'

from PyQt4 import QtCore, QtGui, uic

from vtk_selections_test import Ui_DockWidget


class VTKSelectionsTestView(QtGui.QDockWidget):

    clicked = QtCore.pyqtSignal()

    def __init__(self):
        super(VTKSelectionsTestView, self).__init__()

        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

    def mouseReleaseEvent(self, event):
        event.accept()
        self.clicked.emit()


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication([])

    widget = VTKSelectionsTestView()

    widget.show()

    sys.exit(app.exec_())