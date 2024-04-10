from typing import Dict

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLayout

from streamdeck_ui.api import StreamDeckServer
from .homeassistant import HomeAssistant
from .homeassistant_settings import HomeAssistantSettings
from .button_settings import HomeAssistantButtonSettings

NAME: str = "Home Assistant"

INSTANCE: HomeAssistant = HomeAssistant()


def get_name() -> str:
    return NAME


def get_icon() -> QIcon:
    icon = QIcon()
    icon.addFile(u"./plugins/home-assistant/homeassistant.png")
    return icon


def apply_settings(settings: Dict[str, str]) -> None:
    INSTANCE.apply_settings(settings)


def get_settings_layout(parent, old_settings: Dict[str, str]) -> QLayout:
    return HomeAssistantSettings(parent, old_settings)


def get_button_settings_layout(parent, old_settings: Dict[str, str]) -> QLayout:
    return HomeAssistantButtonSettings(parent, old_settings, INSTANCE)


def apply_button_settings(deck_id: str, page_id: int, button_id: int, button_settings: Dict[str, str]) -> None:
    INSTANCE.apply_button_settings(deck_id, page_id, button_id, button_settings)


def button_pressed(button_settings: Dict[str, str]) -> None:
    entity = button_settings.get("entity")
    service = button_settings.get("service")

    if entity and service:
        INSTANCE.call_service(entity, service)


def initialize(api: StreamDeckServer, settings: Dict[str, str]) -> None:
    INSTANCE.initialize(api, settings)
