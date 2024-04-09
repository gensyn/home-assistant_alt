from typing import Dict

from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QDialogButtonBox, QFormLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QLineEdit, QCheckBox, QDialog)


class HomeAssistantSettings(QFormLayout):
    def __init__(self, parent, old_settings: Dict[str, str], *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.url: None | QLineEdit = None
        self.token: None | QLineEdit = None
        self.port: None | QLineEdit = None
        self.ssl: None | QCheckBox = None

        icon = QIcon()
        icon.addFile(":/icons/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)

        label_url = QLabel(parent)
        label_url.setText("URL")

        self.url = QLineEdit(parent)
        self.url.setMinimumSize(QSize(500, 0))
        self.url.setText(old_settings.get("url", ""))

        label_token = QLabel(parent)
        label_token.setText("Token")

        self.token = QLineEdit(parent)
        self.token.setText(old_settings.get("token", ""))

        label_port = QLabel(parent)
        label_port.setText("Port")

        self.port = QLineEdit(parent)
        self.port.setText(old_settings.get("port", ""))

        label_ssl = QLabel(parent)
        label_ssl.setText("SSL")

        self.ssl = QCheckBox(parent)
        self.ssl.setChecked(old_settings.get("ssl", True))

        self.setWidget(0, QFormLayout.LabelRole, label_url)
        self.setWidget(0, QFormLayout.FieldRole, self.url)
        self.setWidget(1, QFormLayout.LabelRole, label_token)
        self.setWidget(1, QFormLayout.FieldRole, self.token)
        self.setWidget(2, QFormLayout.LabelRole, label_port)
        self.setWidget(2, QFormLayout.FieldRole, self.port)
        self.setWidget(3, QFormLayout.LabelRole, label_ssl)
        self.setWidget(3, QFormLayout.FieldRole, self.ssl)

    def get_settings(self) -> Dict[str, str]:
        return {
            "url": self.url.text(),
            "token": self.token.text(),
            "port": self.port.text(),
            "ssl": self.ssl.isChecked(),
        }
