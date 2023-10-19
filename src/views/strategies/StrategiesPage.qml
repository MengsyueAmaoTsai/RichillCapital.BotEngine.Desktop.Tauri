

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Qt.labs.platform

Page {
    id: root
    horizontalPadding: 64
    rightPadding: 70
    bottomPadding: 20
    background: Rectangle {
        anchors.fill: parent
    }

    DropArea {
        id: dropArea
        anchors.fill: parent
        
        ColumnLayout {
            id: layout
            anchors.fill: parent
            spacing: 0
            
            HorizontalHeaderView {
                id: header
                syncView: table
            }

            TableView {
                id: table
            }            
        }
    }
}