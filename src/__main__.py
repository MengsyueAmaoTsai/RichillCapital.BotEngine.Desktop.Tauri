import sys
import logging
from pathlib import Path
from PySide6.QtCore import QUrl, qWarning
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from datetime import datetime as DateTime
from PySide6.QtQuickControls2 import QQuickStyle

date_format = "%Y-%m-%dT%H:%M:%S.%fZ"

output_template = "%(asctime)s - [%(levelname)s] - %(name)s\n%(message)s"
output_template = output_template.replace("%(asctime)s", f"{DateTime.utcnow().strftime(date_format)}")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(output_template))

log = logging.getLogger("BotEngine.Desktop")
log.addHandler(console_handler)
log.setLevel(logging.DEBUG)


try:
    log.info("Starting application...")
    
    root_path = Path(__file__).parent.parent
    qml_path = root_path / 'src' / 'views' / 'main_window.qml'

    QQuickStyle.setStyle('Fusion')

    app = QGuiApplication(sys.argv)
    app.setOrganizationName("Richill Capital")
    app.setOrganizationDomain("richillcapital.com")
    app.setApplicationName("BotEngine Desktop")
    app.setApplicationDisplayName("BotEngine Desktop")

    engine = QQmlApplicationEngine()
    
    engine.addImportPath(":/") # import path = qrc:/

    # Output import paths to debug console.
    log.info(f"----- QmlEngine import paths -----")
    for path in engine.importPathList():
        print(f"Import path = {path}")
    print("----------------------------------")

    # Load qml
    engine.load(qml_path)
    
    if not engine.rootObjects():
        log.error(f"Can not resolve qml: {qml_path}")
        sys.exit(-1)

    sys.exit(app.exec())

except Exception as exception:
    log.error(f"Unexpected error.\n{exception}")

finally:
    log.info("Shutdown completed.")