# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import flask
import os
import serial
from subprocess import call, Popen

"""
* Control a set of RGBW LED Striplights through OctoPrint
*
* @type {[type]}
"""


class IlluminatrixPlugin(
        octoprint.plugin.StartupPlugin,
        octoprint.plugin.TemplatePlugin,
        octoprint.plugin.EventHandlerPlugin,
        octoprint.plugin.BlueprintPlugin,
        octoprint.plugin.SettingsPlugin
):

    def set_serial_config(self, port):
        try:
            if port:
                ser = serial.Serial(port, 9600)
        except:
            return

            return ser

    def issue_command(self, cmd_str):
        try:
            port = self._settings.get(["Port"])
            ser = self.set_serial_config(port)
            ser.write(b';{0};').format(cmd_str)
            Popen("echo -n \";" + cmd_str + ";\" > " + port, shell=True)
            return flask.make_response("Illuminatrix " + cmd_str + " mode", 750)
        except:
            return

    # StartupPlugin
    def on_after_startup(self):
        self._logger.info("Illuminatrix plugin lives")

    # TemplatePlugin
    def get_template_configs(self):
        return [
            dict(type="tab", custom_bindings=False),
            dict(type="settings", custom_bindings=False),
        ]

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/on", methods=["GET"])
    def on(self):
        return self.issue_command("ON")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/off", methods=["GET"])
    def off(self):
        return self.issue_command("OFF")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/white", methods=["GET"])
    def white(self):
        return self.issue_command("WHITE")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/red", methods=["GET"])
    def red(self):
        return self.issue_command("RED")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/green", methods=["GET"])
    def green(self):
        return self.issue_command("GREEN")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/blue", methods=["GET"])
    def blue(self):
        return self.issue_command("BLUE")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/lightblue", methods=["GET"])
    def lightblue(self):
        return self.issue_command("LIGHTBLUE")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/purple", methods=["GET"])
    def purple(self):
        return self.issue_command("PURPLE")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/yellow", methods=["GET"])
    def yellow(self):
        return self.issue_command("YELLOW")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/standby", methods=["GET"])
    def standby(self):
        return self.issue_command("STANDBY")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/cycleon", methods=["GET"])
    def cycleon(self):
        return self.issue_command("CYCLEON")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/cyclewhite", methods=["GET"])
    def cyclewhite(self):
        return self.issue_command("CYCLEWHITE")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/cyclered", methods=["GET"])
    def cyclered(self):
        return self.issue_command("CYCLERED")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/cyclegreen", methods=["GET"])
    def cyclegreen(self):
        return self.issue_command("CYCLEGREEN")

    # BlueprintPlugin
    @octoprint.plugin.BlueprintPlugin.route("/cycleblue", methods=["GET"])
    def cyclewblue(self):
        return self.issue_command("CYCLEBLUE")

    def is_blueprint_protected(self):
        return False

    """EVENTS"""
    # EventHandlerPlugin
    def on_event(self, event, payload):
        command = self._settings.get([event])
        if command is not None:
            self.issue_command(command)

    """SETTINGS"""
    def get_settings_defaults(self):
        return dict(
            Disconnected="OFF",
            Connected="STANDBY",
            PrintStarted="CYCLEWHITE",
            PrintCancelled="STANDBY",
            PrintFailed="RED",
            PrintPaused="YELLOW",
            PrintResumed="WHITE",
            PrintDone="STANDBY",
            Home="CYCLEGREEN",
            Port="/dev/ttyAMA0",
        )

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False),
            dict(type="tab", custom_bindings=False),
        ]

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginIlluminatrix"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the
# documentation for that.

__plugin_name__ = "Illuminatrix"
__plugin_implementation__ = IlluminatrixPlugin()
