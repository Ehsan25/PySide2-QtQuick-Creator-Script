
# exp: pyside2_creator hms-client

import os
import sys


def create_app(project_name):
    project_path = os.path.join(os.getcwd(), project_name)

    try:
        os.makedirs(project_path + '/ViewFiles')
        f = open(project_path + '/app.py', 'w+')
        f.write("#!/usr/bin/env python\n")
        f.write("# -*- coding: utf-8 -*-\n\n")
        f.write("import os\n")
        f.write("import sys\n")
        f.write("import PySide2.QtQml\n")
        f.write("from OpenGL import GL\n")
        f.write("from PySide2.QtQuick import QQuickView\n")
        f.write("from PySide2.QtCore import Qt, QUrl\n")
        f.write("from PySide2.QtGui import QGuiApplication\n\n\n")
        f.write("if __name__ == '__main__':\n\n")
        f.write("\t# Setup the application window\n")
        f.write("\tapp = QGuiApplication(sys.argv)\n")
        f.write("\tview = QQuickView()\n")
        f.write("\tview.setResizeMode(QQuickView.SizeRootObjectToView)\n\n")
        f.write("\t# Expose a model or a property to the qml code\n\t#\n\t#\n\n")
        f.write("\t# Load the qml file\n")
        f.write("\tcurrent_path = os.path.dirname(__file__)\n")
        f.write("\tqml_file = os.path.join(current_path, 'ViewFiles/MainView.qml')\n")
        f.write("\tview.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))\n\n")
        f.write("\t# Show the window\n")
        f.write("\tif view.status() == QQuickView.Error:\n")
        f.write("\t\tsys.exit(-1)\n")
        f.write("\tview.show()\n\n")
        f.write("\t# Execute and cleanup\n")
        f.write("\tapp.exec_()\n")
        f.write("\tdel view\n\n")
        
        f.close()


        f = open(project_path + '/ViewFiles/MainView.qml', 'w+')
        f.write("import QtQuick 2.12\n")
        f.write("import QtQuick.Controls 2.5\n")
        f.write("import QtQuick.Controls.Material 2.3\n\n")
        f.write("Page {\n")
        f.write("\tid: main\n")
        f.write("\twidth: 640\n")
        f.write("\theight: 480\n")
        f.write("}\n")

        f.close()

    except OSError:
        print('Creation of the directory %s failed' % project_path)
    else:
        print('Successfully created the project %s' % sys.argv[1])


if __name__ == '__main__':
    create_app(sys.argv[1])