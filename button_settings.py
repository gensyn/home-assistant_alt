from typing import Dict

from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QDialogButtonBox, QFormLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QLineEdit, QCheckBox, QDialog, QComboBox)


class HomeAssistantButtonSettings(QFormLayout):
    def __init__(self, parent, old_settings: Dict[str, str], hass, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.domain: None | QComboBox = None
        self.entity: None | QComboBox = None
        self.service: None | QComboBox = None
        self.hass = hass

        icon = QIcon()
        icon.addFile(":/icons/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)

        label_domain = QLabel(parent)
        label_domain.setText("Domain")

        self.domain = QComboBox(parent)
        self.domain.setMinimumSize(QSize(500, 0))
        self.domain.currentTextChanged.connect(self.handle_domain_changed)

        label_entity = QLabel(parent)
        label_entity.setText("Entity")

        self.entity = QComboBox(parent)
        self.entity.setEnabled(False)

        label_service = QLabel(parent)
        label_service.setText("Service")

        self.service = QComboBox(parent)
        self.service.setEnabled(False)

        self.setWidget(0, QFormLayout.LabelRole, label_domain)
        self.setWidget(0, QFormLayout.FieldRole, self.domain)
        self.setWidget(1, QFormLayout.LabelRole, label_entity)
        self.setWidget(1, QFormLayout.FieldRole, self.entity)
        self.setWidget(2, QFormLayout.LabelRole, label_service)
        self.setWidget(2, QFormLayout.FieldRole, self.service)

        old_domain = old_settings.get("domain", "")

        self.load_domains()

        for i in range(self.domain.count()):
            if old_domain == self.domain.itemText(i):
                self.domain.setCurrentIndex(i)

                old_entity = old_settings.get("entity", "")
                old_service = old_settings.get("service", "")

                for j in range(self.entity.count()):
                    if old_entity == self.entity.itemText(j):
                        self.entity.setCurrentIndex(j)

                for k in range(self.service.count()):
                    if old_service == self.service.itemText(k):
                        self.service.setCurrentIndex(k)

                break

    def handle_domain_changed(self):
        self.load_entities()
        self.load_services()

    def load_domains(self):
        self.domain.clear()
        self.domain.addItem("")

        domains = sorted(self.hass.get_domains())

        for domain in domains:
            self.domain.addItem(domain)

    def load_entities(self):
        self.entity.setEnabled(True)
        self.entity.clear()
        self.entity.addItem("")

        entities = sorted(self.hass.get_entities(self.domain.currentText()))

        for entity in entities:
            self.entity.addItem(entity)

    def load_services(self):
        self.service.setEnabled(True)
        self.service.clear()
        self.service.addItem("")

        services = self.hass.get_services(self.domain.currentText())

        for service in services:
            self.service.addItem(service)

    def get_settings(self) -> Dict[str, str]:
        return {
            "domain": self.domain.currentText(),
            "entity": self.entity.currentText(),
            "service": self.service.currentText(),
        }
