#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file
# @author (C) 2015 by Roman Khassraf <rkhassraf@gmail.com>
# @section LICENSE
# 
# Gr-gsm is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# Gr-gsm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with gr-gsm; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
# 

from gnuradio import gr, gr_unittest, blocks
import grgsm_swig as grgsm
import pmt

class qa_burst_timeslot_splitter (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001 (self):
        """
            24 random framenumbers, timeslots and bursts as input
        """
        framenumbers_input = [1259192, 1076346, 1076242, 235879, 1259218, 2194302, 2714322, 1588, 1259244, 1563637, 1435624, 1928543, 503726, 1571144, 2658397, 1807445, 869789, 624070, 2005511, 1306953, 2284894, 1600339, 551375, 1259270]
        timeslots_input = [6, 3, 4, 3, 5, 3, 2, 7, 1, 6, 0, 7, 2, 3, 2, 0, 7, 1, 0, 6, 0, 6, 5, 7]
        bursts_input = [
            "0001100001000111100111101111100101000100101011000010011110011101001111101100010100111111100000110100011111101011101100100111110011000100010001010000",
            "0001000101000000001001111110000110010110110111110111101000001101001111101100010100111111001110001001110101110001010001000111011010010001011011000000",
            "0001001101101101000111001000101011001101001110110001001100111101001111101100010100111111111001001010011010011111010010010101011001001011011100110000",
            "0000010010100000001001101010100001011100010001101100111111101101001111101100010100111111101101001110100010101110010110101111100010010000110010110000",
            "0000010101010110010011110101010101101100000000001000100100101010000111011101001000011101011101110000101011001111000100001000000000001110010001111000",
            "0001000000000010111010100000010101000010001010111010000000011010000111011101001000011101000000100010111110101000000001000000000010111010100000000000",
            "0001010101111111111010000001010101011111111111101000000001001010000111011101001000011101010111111111111010101000000001010101011011101010000001000000",
            "0000000000111110101010100001000000100010101110101010000101001010000111011101001000011101001010001111101010001000010000000000101110101010100000010000",
            "0000010000000010000001001000011001010010000011000101000000001010000111011101001000011101010100100000000001001000001000000100100011000101001000111000",
            "0001010100110111100000110111100110010100011100011000110110001010000111011101001000011101011111111001111001101010010100000000011111001101000111110000",
            "0001100110000001011110001000001100101001010100111111000100111010000111011101001000011101000011010010001010111101000100110011111010100010010101000000",
            "0000010101100101010110000011010000000000000010111001110110101010000111011101001000011101000001000100100001111001100011000101010001110001010100111000",
            "0001000100000011001010111001111100011010000000000000001001001010000111011101001000011101010110000101111010011001110110001001011010101000011110110000",
            "0001100001000111111111100001011000000011010110111010110000111010000111011101001000011101100010111100100101110001101000110100110000001010101110011000",
            "0000000100111011000000000010100100001100101010000000010010101010000111011101001000011101000110110001110110000100110100110110011001100100000101100000",
            "0000100101111010011110111010100111010100011011011101100111001010000111011101001000011101010000111010000110100000001000010011101011001001110100011000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0000110101000011011010110000110011010000000001001010110010001010000111011101001000011101010000011000111001101110000000110010100001101110101000100000",
            "0000001000010001011111111111101010100000010101011101101010101010000111011101001000011101100010010101010101011110101010101000010001011101111010101000",
            "0000101110101111011001011001000011110010100010011100110010001010000111011101001000011101100000001110000100010100110111001001100010101101100010101000",
            "0001100010000001000111011100101101101010100001111101001000101010000111011101001000011101111010000011010110010111011111010010001000001101100011111000",
            "0001011101101101011100001111001100010001000011011001101110011010000111011101001000011101010010111011100111000001011100100001111010100101111000100000",
            "0000001000100011000000000000110100000000010000001010100100001010000111011101001000011101000010010000000000001001000001011000000001010000000100010000",
            "0000100000110001000000000100000110001011100001001000000000001010000111011101001000011101001010010001010000000111010000000011000001000000000101010000"
        ]

        bursts_expected_0 = [
            "0001100110000001011110001000001100101001010100111111000100111010000111011101001000011101000011010010001010111101000100110011111010100010010101000000",
            "0000100101111010011110111010100111010100011011011101100111001010000111011101001000011101010000111010000110100000001000010011101011001001110100011000",
            "0000001000010001011111111111101010100000010101011101101010101010000111011101001000011101100010010101010101011110101010101000010001011101111010101000",
            "0001100010000001000111011100101101101010100001111101001000101010000111011101001000011101111010000011010110010111011111010010001000001101100011111000"
        ]
        
        bursts_expected_1 = [
            "0000010000000010000001001000011001010010000011000101000000001010000111011101001000011101010100100000000001001000001000000100100011000101001000111000",
            "0000110101000011011010110000110011010000000001001010110010001010000111011101001000011101010000011000111001101110000000110010100001101110101000100000"
        ]
        
        bursts_expected_2 = [
            "0001010101111111111010000001010101011111111111101000000001001010000111011101001000011101010111111111111010101000000001010101011011101010000001000000",
            "0001000100000011001010111001111100011010000000000000001001001010000111011101001000011101010110000101111010011001110110001001011010101000011110110000",
            "0000000100111011000000000010100100001100101010000000010010101010000111011101001000011101000110110001110110000100110100110110011001100100000101100000"
        ]
        
        bursts_expected_3 = [
            "0001000101000000001001111110000110010110110111110111101000001101001111101100010100111111001110001001110101110001010001000111011010010001011011000000",
            "0000010010100000001001101010100001011100010001101100111111101101001111101100010100111111101101001110100010101110010110101111100010010000110010110000",
            "0001000000000010111010100000010101000010001010111010000000011010000111011101001000011101000000100010111110101000000001000000000010111010100000000000",
            "0001100001000111111111100001011000000011010110111010110000111010000111011101001000011101100010111100100101110001101000110100110000001010101110011000"
        ]
        
        bursts_expected_4 = [
            "0001001101101101000111001000101011001101001110110001001100111101001111101100010100111111111001001010011010011111010010010101011001001011011100110000"
        ]
        
        bursts_expected_5 = [
            "0000010101010110010011110101010101101100000000001000100100101010000111011101001000011101011101110000101011001111000100001000000000001110010001111000",
            "0000001000100011000000000000110100000000010000001010100100001010000111011101001000011101000010010000000000001001000001011000000001010000000100010000"
        ]
        
        bursts_expected_6 = [
            "0001100001000111100111101111100101000100101011000010011110011101001111101100010100111111100000110100011111101011101100100111110011000100010001010000",
            "0001010100110111100000110111100110010100011100011000110110001010000111011101001000011101011111111001111001101010010100000000011111001101000111110000",
            "0000101110101111011001011001000011110010100010011100110010001010000111011101001000011101100000001110000100010100110111001001100010101101100010101000",
            "0001011101101101011100001111001100010001000011011001101110011010000111011101001000011101010010111011100111000001011100100001111010100101111000100000"
        ]
        
        bursts_expected_7 = [
            "0000000000111110101010100001000000100010101110101010000101001010000111011101001000011101001010001111101010001000010000000000101110101010100000010000",
            "0000010101100101010110000011010000000000000010111001110110101010000111011101001000011101000001000100100001111001100011000101010001110001010100111000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0000100000110001000000000100000110001011100001001000000000001010000111011101001000011101001010010001010000000111010000000011000001000000000101010000"
        ]


        src = grgsm.burst_source(framenumbers_input, timeslots_input, bursts_input)
        splitter = grgsm.burst_timeslot_splitter()
        sink_0 = grgsm.burst_sink()
        sink_1 = grgsm.burst_sink()
        sink_2 = grgsm.burst_sink()
        sink_3 = grgsm.burst_sink()
        sink_4 = grgsm.burst_sink()
        sink_5 = grgsm.burst_sink()
        sink_6 = grgsm.burst_sink()
        sink_7 = grgsm.burst_sink()

        self.tb.msg_connect(src, "out", splitter, "in")
        self.tb.msg_connect(splitter, "out0", sink_0, "in")
        self.tb.msg_connect(splitter, "out1", sink_1, "in")
        self.tb.msg_connect(splitter, "out2", sink_2, "in")
        self.tb.msg_connect(splitter, "out3", sink_3, "in")
        self.tb.msg_connect(splitter, "out4", sink_4, "in")
        self.tb.msg_connect(splitter, "out5", sink_5, "in")
        self.tb.msg_connect(splitter, "out6", sink_6, "in")
        self.tb.msg_connect(splitter, "out7", sink_7, "in")

        self.tb.run ()

        bursts_result_0 = list(sink_0.get_burst_data())
        bursts_result_1 = list(sink_1.get_burst_data())
        bursts_result_2 = list(sink_2.get_burst_data())
        bursts_result_3 = list(sink_3.get_burst_data())
        bursts_result_4 = list(sink_4.get_burst_data())
        bursts_result_5 = list(sink_5.get_burst_data())
        bursts_result_6 = list(sink_6.get_burst_data())
        bursts_result_7 = list(sink_7.get_burst_data())
        
        self.assertEqual(bursts_expected_0, bursts_result_0)
        self.assertEqual(bursts_expected_1, bursts_result_1)
        self.assertEqual(bursts_expected_2, bursts_result_2)
        self.assertEqual(bursts_expected_3, bursts_result_3)
        self.assertEqual(bursts_expected_4, bursts_result_4)
        self.assertEqual(bursts_expected_5, bursts_result_5)
        self.assertEqual(bursts_expected_6, bursts_result_6)
        self.assertEqual(bursts_expected_7, bursts_result_7)


if __name__ == '__main__':
    gr_unittest.run(qa_burst_timeslot_splitter, "qa_burst_timeslot_splitter.xml")
