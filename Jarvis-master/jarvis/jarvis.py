# -*- coding:utf-8 -*-
import logging

from config import *
from speak import speak_out
from chatrobot import talk

logger = logging.getLogger(__name__)


class Jarvis(object):
    # Built-in words

    @classmethod
    def handle_action(cls, command, **kwargs):
        """
        Handles a single text command.
        """
        # Use lowercase for processing.
        command = command.lower()
        logger.debug("Received command: '%s'", command)

        # Determine if this is an actionable command.
        if any(cognate in command for cognate in XIAOBING_COGNATES):
            # output_info(YES_SIR)
            do_action(command)


def do_action(command):
    try:
        is_exist = False
        for action in ACTION_LIST:
            if action['in_msg'] in command:
                output_info(action['out_msg'])
                if action['command']:
                    msg, url = action['command']()
                    if msg:
                        output_info(msg.decode("utf-8"))
                    if url:
                        logger.info(url)
                is_exist = True
        if is_exist == False:
            for cognate in XIAOBING_COGNATES:
                if cognate in command:
                    command = command.replace(cognate, u'')
            # output_info(YES_SIR)
            if command:
                # output_info(YES_SIR)
                do_action_according_to_robot(command)
            else:
                output_info(YES_SIR)
    except Exception, e:
        pass


def do_action_according_to_robot(command):
    try:
        msg, url = talk(command)
        if msg:
            output_info(msg.decode("utf-8"))
        if url:
            logger.info(url)
    except Exception, e:
        pass


def output_info(msg):
    logger.info(msg)
    speak_out(msg)
