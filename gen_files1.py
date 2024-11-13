# -*- encoding: utf-8 -*-

import os
import sys
import re
import shutil

ss_files_content = """
static const uint8_t _3f00_def[] = {0x62,0x1b,0x82,0x02,0x78,0x21,0x83,0x02,0x3f,0x00,0xa5,0x09,0x80,0x01,0xf1,0x87,0x01,0x00,0x88,0x01,0x00,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x0f};
static const uint8_t _3f00_2f00[] = {0x61,0x19,0x4f,0x10,0xa0,0x00,0x00,0x00,0x87,0x10,0x02,0xff,0xff,0xff,0xff,0x89,0x07,0x09,0x00,0x00,0x50,0x05,0x55,0x53,0x69,0x6d,0x31,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_2f00_def[] = {0x62,0x1a,0x82,0x05,0x42,0x21,0x00,0x26,0x02,0x83,0x02,0x2f,0x00,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x02,0x80,0x02,0x00,0x4c,0x88,0x01,0xf0};
static const uint8_t _3f00_2f05[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_2f05_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x2f,0x05,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x01,0x80,0x02,0x00,0x0a,0x88,0x01,0x28};
static const uint8_t _3f00_2f06[] = {0x80,0x01,0x01,0x90,0x00,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x01,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0x90,0x00,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0x90,0x00,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0xa4,0x06,0x83,0x01,0x01,0x95,0x01,0x08,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x01,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0xa4,0x06,0x83,0x01,0x01,0x95,0x01,0x08,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_2f06_def[] = {0x62,0x1a,0x82,0x05,0x42,0x21,0x00,0x28,0x10,0x83,0x02,0x2f,0x06,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x02,0x80,0x02,0x02,0x80,0x88,0x01,0x30};
static const uint8_t _3f00_2f08[] = {0x3c,0x05,0x02,0x00,0x00};
static const uint8_t _3f00_2f08_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x2f,0x08,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x02,0x80,0x02,0x00,0x05,0x88,0x01,0x40};
static const uint8_t _3f00_2fe2[] = {0x00,0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99};
static const uint8_t _3f00_2fe2_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x2f,0xe2,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x03,0x80,0x02,0x00,0x0a,0x88,0x01,0x10};
static const uint8_t _3f00_5f100001[] = {0xff,0xff,0x2f,0xe2,0xff,0xff,0xff,0xff,0x2f,0x05,0x2f,0x06,0xff,0xff,0x2f,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x2f,0x00,0xff,0xff};
static const uint8_t _3f00_5f100001_def[] = {0x62,0x10,0x82,0x05,0x02,0x21,0x00,0x02,0x1f,0x83,0x04,0x5f,0x10,0x00,0x01,0x80,0x01,0x3e};
static const uint8_t _3f00_7ff0_def[] = {0x62,0x22,0x82,0x02,0x78,0x21,0x83,0x02,0x7f,0xf0,0x84,0x10,0xa0,0x00,0x00,0x00,0x87,0x10,0x02,0xff,0xff,0xff,0xff,0x89,0x07,0x09,0x00,0x00,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x0f};
static const uint8_t _3f00_7ff0_5f100001[] = {0x6f,0xb7,0x6f,0x05,0x6f,0xe3,0xff,0xff,0xff,0xff,0x6f,0x78,0x6f,0x07,0x6f,0x08,0x6f,0x09,0xff,0xff,0x6f,0x7e,0x6f,0x73,0x6f,0x7b,0xff,0xff,0x6f,0x5b,0x6f,0x5c,0xff,0xff,0x6f,0x31,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x6f,0x06,0x6f,0xe4,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_5f100001_def[] = {0x62,0x10,0x82,0x05,0x02,0x21,0x00,0x02,0x1f,0x83,0x04,0x5f,0x10,0x00,0x01,0x80,0x01,0x3e};
static const uint8_t _3f00_7ff0_6f05[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6f05_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x05,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x01,0x80,0x02,0x00,0x0a,0x88,0x01,0x10};
static const uint8_t _3f00_7ff0_6f06[] = {0x80,0x01,0x01,0x90,0x00,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x01,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0x90,0x00,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0x90,0x00,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0xa4,0x06,0x83,0x01,0x01,0x95,0x01,0x08,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x01,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0xa4,0x06,0x83,0x01,0x01,0x95,0x01,0x08,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80,0x01,0x01,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0x80,0x01,0x02,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0x80,0x01,0x00,0xa4,0x06,0x83,0x01,0x0a,0x95,0x01,0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6f06_def[] = {0x62,0x1a,0x82,0x05,0x42,0x21,0x00,0x28,0x10,0x83,0x02,0x6f,0x06,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x02,0x80,0x02,0x02,0x80,0x88,0x01,0xb8};
static const uint8_t _3f00_7ff0_6f07[] = {0x08,0x49,0x10,0x10,0x00,0x00,0x00,0x00,0x10};
static const uint8_t _3f00_7ff0_6f07_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x07,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x05,0x80,0x02,0x00,0x09,0x88,0x01,0x38};
static const uint8_t _3f00_7ff0_6f08[] = {0x07,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6f08_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x08,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x21,0x88,0x01,0x40};
static const uint8_t _3f00_7ff0_6f09[] = {0x07,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6f09_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x09,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x21,0x88,0x01,0x48};
static const uint8_t _3f00_7ff0_6f31[] = {0x05};
static const uint8_t _3f00_7ff0_6f31_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x31,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x05,0x80,0x02,0x00,0x01,0x88,0x01,0x90};
static const uint8_t _3f00_7ff0_6f38[] = {0x00,0x08,0x00,0x0c,0x21,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_7ff0_6f38_def[] = {0x62,0x16,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x38,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x05,0x80,0x02,0x00,0x0f,0x88,0x00};
static const uint8_t _3f00_7ff0_6f42[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xe5,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x07,0x91,0x44,0x77,0x79,0x07,0x84,0x84,0xff,0xff,0xff,0xff,0xff,0x00,0xa8,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6f42_def[] = {0x62,0x19,0x82,0x05,0x42,0x21,0x00,0x34,0x02,0x83,0x02,0x6f,0x42,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x02,0x80,0x02,0x00,0x68,0x88,0x00};
static const uint8_t _3f00_7ff0_6f5b[] = {0xf0,0x00,0x00,0xf0,0x00,0x00};
static const uint8_t _3f00_7ff0_6f5b_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x5b,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x06,0x88,0x01,0x78};
static const uint8_t _3f00_7ff0_6f5c[] = {0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6f5c_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x5c,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x05,0x80,0x02,0x00,0x03,0x88,0x01,0x80};
static const uint8_t _3f00_7ff0_6f73[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0x00,0xff,0x01};
static const uint8_t _3f00_7ff0_6f73_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x73,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x0e,0x88,0x01,0x60};
static const uint8_t _3f00_7ff0_6f78[] = {0x03,0xff};
static const uint8_t _3f00_7ff0_6f78_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x78,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x05,0x80,0x02,0x00,0x02,0x88,0x01,0x30};
static const uint8_t _3f00_7ff0_6f7b[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6f7b_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x7b,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x0c,0x88,0x01,0x68};
static const uint8_t _3f00_7ff0_6f7e[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0xff,0x01};
static const uint8_t _3f00_7ff0_6f7e_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0x7e,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x0b,0x88,0x01,0x58};
static const uint8_t _3f00_7ff0_6fad[] = {0x01,0x00,0x08,0x03};
static const uint8_t _3f00_7ff0_6fad_def[] = {0x62,0x16,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0xad,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x02,0x80,0x02,0x00,0x04,0x88,0x00};
static const uint8_t _3f00_7ff0_6fb7[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00};
static const uint8_t _3f00_7ff0_6fb7_def[] = {0x62,0x1a,0x82,0x05,0x42,0x21,0x00,0x10,0x05,0x83,0x02,0x6f,0xb7,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x02,0x80,0x02,0x00,0x50,0x88,0x01,0x08};
static const uint8_t _3f00_7ff0_6fc4[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6fc4_def[] = {0x62,0x16,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0xc4,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x40,0x88,0x00};
static const uint8_t _3f00_7ff0_6fe3[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0x01};
static const uint8_t _3f00_7ff0_6fe3_def[] = {0x62,0x17,0x82,0x02,0x41,0x21,0x83,0x02,0x6f,0xe3,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x12,0x88,0x01,0x18};
static const uint8_t _3f00_7ff0_6fe4[] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_7ff0_6fe4_def[] = {0x62,0x1a,0x82,0x05,0x42,0x21,0x00,0x36,0x01,0x83,0x02,0x6f,0xe4,0x8a,0x01,0x05,0x8b,0x03,0x6f,0x06,0x04,0x80,0x02,0x00,0x36,0x88,0x01,0xc0};
static const uint8_t _3f00_a001[] = {0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f,0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,0x1e,0x1f,0x00};
static const uint8_t _3f00_a001_def[] = {0x62,0x16,0x82,0x02,0x41,0x21,0x83,0x02,0xa0,0x01,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x06,0x80,0x02,0x00,0x21,0x88,0x00};
static const uint8_t _3f00_a003[] = {0x00,0x03,0x00,0x0a,0x00,0x01,0x31,0x32,0x33,0x34,0xff,0xff,0xff,0xff,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x00,0x03,0x00,0x0a,0x00,0x81,0x31,0x32,0x33,0x34,0xff,0xff,0xff,0xff,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x01,0x03,0x00,0x00,0x00,0x0a,0x31,0x32,0x33,0x34,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_a003_def[] = {0x62,0x19,0x82,0x05,0x42,0x21,0x00,0x16,0x03,0x83,0x02,0xa0,0x03,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x06,0x80,0x02,0x00,0x42,0x88,0x00};
static const uint8_t _3f00_a004[] = {0xb0,0x00,0x11,0x06,0x03,0x03,0x00,0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,0xaa,0xbb,0xcc,0xdd,0xee,0xff,0x01,0x23,0x45,0x67,0x89,0xab,0xcd,0xef,0x01,0x23,0x45,0x67,0x01,0x23,0x45,0x67,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_a004_def[] = {0x62,0x19,0x82,0x05,0x42,0x21,0x00,0x26,0x03,0x83,0x02,0xa0,0x04,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x06,0x80,0x02,0x00,0x72,0x88,0x00};
static const uint8_t _3f00_a005[] = {0xb0,0x00,0x11,0xff,0xff,0xff,0x00,0x00,0x00,0x00,0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_a005_def[] = {0x62,0x19,0x82,0x05,0x42,0x21,0x00,0x0b,0x03,0x83,0x02,0xa0,0x05,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x06,0x80,0x02,0x00,0x21,0x88,0x00};
static const uint8_t _3f00_a100[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a100_def[] = {0x62,0x16,0x82,0x02,0x41,0x21,0x83,0x02,0xa1,0x00,0x8a,0x01,0x05,0x8b,0x03,0x2f,0x06,0x06,0x80,0x02,0x00,0x08,0x88,0x00};
static const uint8_t _3f00_a101[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a102[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a103[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a104[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a105[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a106[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a107[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a108[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a109[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a10a[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a10b[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a10c[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a10d[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a10e[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a10f[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a110[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a111[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a112[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a113[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a114[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a115[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a116[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a117[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a118[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a119[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a11a[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a11b[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a11c[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a11d[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a11e[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a11f[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
static const uint8_t _3f00_a120[] = {0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00};
static const uint8_t _3f00_a1df1d01[] = {0xa0,0x00,0x00,0x00,0x87,0x10,0x02,0xff,0xff,0xff,0xff,0x89,0x07,0x09,0x00,0x00,0x7f,0xf0,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};
static const uint8_t _3f00_a1df1d01_def[] = {0x62,0x11,0x82,0x05,0x02,0x21,0x00,0x12,0x10,0x83,0x04,0xa1,0xdf,0x1d,0x01,0x80,0x02,0x01,0x20};

"""

ss_files_arr = """
{.name = "ss_3f00.def", .data = _3f00_def, .size = sizeof(_3f00_def)}, 
{.name = "ss_3f00_2f00", .data = _3f00_2f00, .size = sizeof(_3f00_2f00)}, 
{.name = "ss_3f00_2f00.def", .data = _3f00_2f00_def, .size = sizeof(_3f00_2f00_def)}, 
{.name = "ss_3f00_2f05", .data = _3f00_2f05, .size = sizeof(_3f00_2f05)}, 
{.name = "ss_3f00_2f05.def", .data = _3f00_2f05_def, .size = sizeof(_3f00_2f05_def)}, 
{.name = "ss_3f00_2f06", .data = _3f00_2f06, .size = sizeof(_3f00_2f06)}, 
{.name = "ss_3f00_2f06.def", .data = _3f00_2f06_def, .size = sizeof(_3f00_2f06_def)}, 
{.name = "ss_3f00_2f08", .data = _3f00_2f08, .size = sizeof(_3f00_2f08)}, 
{.name = "ss_3f00_2f08.def", .data = _3f00_2f08_def, .size = sizeof(_3f00_2f08_def)}, 
{.name = "ss_3f00_2fe2", .data = _3f00_2fe2, .size = sizeof(_3f00_2fe2)}, 
{.name = "ss_3f00_2fe2.def", .data = _3f00_2fe2_def, .size = sizeof(_3f00_2fe2_def)}, 
{.name = "ss_3f00_5f100001", .data = _3f00_5f100001, .size = sizeof(_3f00_5f100001)}, 
{.name = "ss_3f00_5f100001.def", .data = _3f00_5f100001_def, .size = sizeof(_3f00_5f100001_def)}, 
{.name = "ss_3f00_7ff0.def", .data = _3f00_7ff0_def, .size = sizeof(_3f00_7ff0_def)}, 
{.name = "ss_3f00_7ff0_5f100001", .data = _3f00_7ff0_5f100001, .size = sizeof(_3f00_7ff0_5f100001)}, 
{.name = "ss_3f00_7ff0_5f100001.def", .data = _3f00_7ff0_5f100001_def, .size = sizeof(_3f00_7ff0_5f100001_def)}, 
{.name = "ss_3f00_7ff0_6f05", .data = _3f00_7ff0_6f05, .size = sizeof(_3f00_7ff0_6f05)}, 
{.name = "ss_3f00_7ff0_6f05.def", .data = _3f00_7ff0_6f05_def, .size = sizeof(_3f00_7ff0_6f05_def)}, 
{.name = "ss_3f00_7ff0_6f06", .data = _3f00_7ff0_6f06, .size = sizeof(_3f00_7ff0_6f06)}, 
{.name = "ss_3f00_7ff0_6f06.def", .data = _3f00_7ff0_6f06_def, .size = sizeof(_3f00_7ff0_6f06_def)}, 
{.name = "ss_3f00_7ff0_6f07", .data = _3f00_7ff0_6f07, .size = sizeof(_3f00_7ff0_6f07)}, 
{.name = "ss_3f00_7ff0_6f07.def", .data = _3f00_7ff0_6f07_def, .size = sizeof(_3f00_7ff0_6f07_def)}, 
{.name = "ss_3f00_7ff0_6f08", .data = _3f00_7ff0_6f08, .size = sizeof(_3f00_7ff0_6f08)}, 
{.name = "ss_3f00_7ff0_6f08.def", .data = _3f00_7ff0_6f08_def, .size = sizeof(_3f00_7ff0_6f08_def)}, 
{.name = "ss_3f00_7ff0_6f09", .data = _3f00_7ff0_6f09, .size = sizeof(_3f00_7ff0_6f09)}, 
{.name = "ss_3f00_7ff0_6f09.def", .data = _3f00_7ff0_6f09_def, .size = sizeof(_3f00_7ff0_6f09_def)}, 
{.name = "ss_3f00_7ff0_6f31", .data = _3f00_7ff0_6f31, .size = sizeof(_3f00_7ff0_6f31)}, 
{.name = "ss_3f00_7ff0_6f31.def", .data = _3f00_7ff0_6f31_def, .size = sizeof(_3f00_7ff0_6f31_def)}, 
{.name = "ss_3f00_7ff0_6f38", .data = _3f00_7ff0_6f38, .size = sizeof(_3f00_7ff0_6f38)}, 
{.name = "ss_3f00_7ff0_6f38.def", .data = _3f00_7ff0_6f38_def, .size = sizeof(_3f00_7ff0_6f38_def)}, 
{.name = "ss_3f00_7ff0_6f42", .data = _3f00_7ff0_6f42, .size = sizeof(_3f00_7ff0_6f42)}, 
{.name = "ss_3f00_7ff0_6f42.def", .data = _3f00_7ff0_6f42_def, .size = sizeof(_3f00_7ff0_6f42_def)}, 
{.name = "ss_3f00_7ff0_6f5b", .data = _3f00_7ff0_6f5b, .size = sizeof(_3f00_7ff0_6f5b)}, 
{.name = "ss_3f00_7ff0_6f5b.def", .data = _3f00_7ff0_6f5b_def, .size = sizeof(_3f00_7ff0_6f5b_def)}, 
{.name = "ss_3f00_7ff0_6f5c", .data = _3f00_7ff0_6f5c, .size = sizeof(_3f00_7ff0_6f5c)}, 
{.name = "ss_3f00_7ff0_6f5c.def", .data = _3f00_7ff0_6f5c_def, .size = sizeof(_3f00_7ff0_6f5c_def)}, 
{.name = "ss_3f00_7ff0_6f73", .data = _3f00_7ff0_6f73, .size = sizeof(_3f00_7ff0_6f73)}, 
{.name = "ss_3f00_7ff0_6f73.def", .data = _3f00_7ff0_6f73_def, .size = sizeof(_3f00_7ff0_6f73_def)}, 
{.name = "ss_3f00_7ff0_6f78", .data = _3f00_7ff0_6f78, .size = sizeof(_3f00_7ff0_6f78)}, 
{.name = "ss_3f00_7ff0_6f78.def", .data = _3f00_7ff0_6f78_def, .size = sizeof(_3f00_7ff0_6f78_def)}, 
{.name = "ss_3f00_7ff0_6f7b", .data = _3f00_7ff0_6f7b, .size = sizeof(_3f00_7ff0_6f7b)}, 
{.name = "ss_3f00_7ff0_6f7b.def", .data = _3f00_7ff0_6f7b_def, .size = sizeof(_3f00_7ff0_6f7b_def)}, 
{.name = "ss_3f00_7ff0_6f7e", .data = _3f00_7ff0_6f7e, .size = sizeof(_3f00_7ff0_6f7e)}, 
{.name = "ss_3f00_7ff0_6f7e.def", .data = _3f00_7ff0_6f7e_def, .size = sizeof(_3f00_7ff0_6f7e_def)}, 
{.name = "ss_3f00_7ff0_6fad", .data = _3f00_7ff0_6fad, .size = sizeof(_3f00_7ff0_6fad)}, 
{.name = "ss_3f00_7ff0_6fad.def", .data = _3f00_7ff0_6fad_def, .size = sizeof(_3f00_7ff0_6fad_def)}, 
{.name = "ss_3f00_7ff0_6fb7", .data = _3f00_7ff0_6fb7, .size = sizeof(_3f00_7ff0_6fb7)}, 
{.name = "ss_3f00_7ff0_6fb7.def", .data = _3f00_7ff0_6fb7_def, .size = sizeof(_3f00_7ff0_6fb7_def)}, 
{.name = "ss_3f00_7ff0_6fc4", .data = _3f00_7ff0_6fc4, .size = sizeof(_3f00_7ff0_6fc4)}, 
{.name = "ss_3f00_7ff0_6fc4.def", .data = _3f00_7ff0_6fc4_def, .size = sizeof(_3f00_7ff0_6fc4_def)}, 
{.name = "ss_3f00_7ff0_6fe3", .data = _3f00_7ff0_6fe3, .size = sizeof(_3f00_7ff0_6fe3)}, 
{.name = "ss_3f00_7ff0_6fe3.def", .data = _3f00_7ff0_6fe3_def, .size = sizeof(_3f00_7ff0_6fe3_def)}, 
{.name = "ss_3f00_7ff0_6fe4", .data = _3f00_7ff0_6fe4, .size = sizeof(_3f00_7ff0_6fe4)}, 
{.name = "ss_3f00_7ff0_6fe4.def", .data = _3f00_7ff0_6fe4_def, .size = sizeof(_3f00_7ff0_6fe4_def)}, 
{.name = "ss_3f00_a001", .data = _3f00_a001, .size = sizeof(_3f00_a001)}, 
{.name = "ss_3f00_a001.def", .data = _3f00_a001_def, .size = sizeof(_3f00_a001_def)}, 
{.name = "ss_3f00_a003", .data = _3f00_a003, .size = sizeof(_3f00_a003)}, 
{.name = "ss_3f00_a003.def", .data = _3f00_a003_def, .size = sizeof(_3f00_a003_def)}, 
{.name = "ss_3f00_a004", .data = _3f00_a004, .size = sizeof(_3f00_a004)}, 
{.name = "ss_3f00_a004.def", .data = _3f00_a004_def, .size = sizeof(_3f00_a004_def)}, 
{.name = "ss_3f00_a005", .data = _3f00_a005, .size = sizeof(_3f00_a005)}, 
{.name = "ss_3f00_a005.def", .data = _3f00_a005_def, .size = sizeof(_3f00_a005_def)}, 
{.name = "ss_3f00_a100", .data = _3f00_a100, .size = sizeof(_3f00_a100)}, 
{.name = "ss_3f00_a100.def", .data = _3f00_a100_def, .size = sizeof(_3f00_a100_def)}, 
{.name = "ss_3f00_a101", .data = _3f00_a101, .size = sizeof(_3f00_a101)}, 
{.name = "ss_3f00_a102", .data = _3f00_a102, .size = sizeof(_3f00_a102)}, 
{.name = "ss_3f00_a103", .data = _3f00_a103, .size = sizeof(_3f00_a103)}, 
{.name = "ss_3f00_a104", .data = _3f00_a104, .size = sizeof(_3f00_a104)}, 
{.name = "ss_3f00_a105", .data = _3f00_a105, .size = sizeof(_3f00_a105)}, 
{.name = "ss_3f00_a106", .data = _3f00_a106, .size = sizeof(_3f00_a106)}, 
{.name = "ss_3f00_a107", .data = _3f00_a107, .size = sizeof(_3f00_a107)}, 
{.name = "ss_3f00_a108", .data = _3f00_a108, .size = sizeof(_3f00_a108)}, 
{.name = "ss_3f00_a109", .data = _3f00_a109, .size = sizeof(_3f00_a109)}, 
{.name = "ss_3f00_a10a", .data = _3f00_a10a, .size = sizeof(_3f00_a10a)}, 
{.name = "ss_3f00_a10b", .data = _3f00_a10b, .size = sizeof(_3f00_a10b)}, 
{.name = "ss_3f00_a10c", .data = _3f00_a10c, .size = sizeof(_3f00_a10c)}, 
{.name = "ss_3f00_a10d", .data = _3f00_a10d, .size = sizeof(_3f00_a10d)}, 
{.name = "ss_3f00_a10e", .data = _3f00_a10e, .size = sizeof(_3f00_a10e)}, 
{.name = "ss_3f00_a10f", .data = _3f00_a10f, .size = sizeof(_3f00_a10f)}, 
{.name = "ss_3f00_a110", .data = _3f00_a110, .size = sizeof(_3f00_a110)}, 
{.name = "ss_3f00_a111", .data = _3f00_a111, .size = sizeof(_3f00_a111)}, 
{.name = "ss_3f00_a112", .data = _3f00_a112, .size = sizeof(_3f00_a112)}, 
{.name = "ss_3f00_a113", .data = _3f00_a113, .size = sizeof(_3f00_a113)}, 
{.name = "ss_3f00_a114", .data = _3f00_a114, .size = sizeof(_3f00_a114)}, 
{.name = "ss_3f00_a115", .data = _3f00_a115, .size = sizeof(_3f00_a115)}, 
{.name = "ss_3f00_a116", .data = _3f00_a116, .size = sizeof(_3f00_a116)}, 
{.name = "ss_3f00_a117", .data = _3f00_a117, .size = sizeof(_3f00_a117)}, 
{.name = "ss_3f00_a118", .data = _3f00_a118, .size = sizeof(_3f00_a118)}, 
{.name = "ss_3f00_a119", .data = _3f00_a119, .size = sizeof(_3f00_a119)}, 
{.name = "ss_3f00_a11a", .data = _3f00_a11a, .size = sizeof(_3f00_a11a)}, 
{.name = "ss_3f00_a11b", .data = _3f00_a11b, .size = sizeof(_3f00_a11b)}, 
{.name = "ss_3f00_a11c", .data = _3f00_a11c, .size = sizeof(_3f00_a11c)}, 
{.name = "ss_3f00_a11d", .data = _3f00_a11d, .size = sizeof(_3f00_a11d)}, 
{.name = "ss_3f00_a11e", .data = _3f00_a11e, .size = sizeof(_3f00_a11e)}, 
{.name = "ss_3f00_a11f", .data = _3f00_a11f, .size = sizeof(_3f00_a11f)}, 
{.name = "ss_3f00_a120", .data = _3f00_a120, .size = sizeof(_3f00_a120)}, 
{.name = "ss_3f00_a1df1d01", .data = _3f00_a1df1d01, .size = sizeof(_3f00_a1df1d01)}, 
{.name = "ss_3f00_a1df1d01.def", .data = _3f00_a1df1d01_def, .size = sizeof(_3f00_a1df1d01_def)}
"""

def main():
    option_str  = r"^\s*(\w+)\s*(\w+)\s*(\w+)\s*(\w+)\[\]\s*=\s*\{([\w|\W]+)\}"
    file_content_dict = {}
    for x in ss_files_content.splitlines():
        if re.search(option_str, x) != None:
            name = re.search(option_str, x).group(4)
            value= re.search(option_str, x).group(5)
            file_content_dict[name] = value

    option_str  = r"\"([\w|\W]+)\"\s*,\s*.data\s*=\s*(\w+)"
    filename_dict = {}
    for x in ss_files_arr.splitlines():
        if re.search(option_str, x) != None:
            name = re.search(option_str, x).group(1)
            value= re.search(option_str, x).group(2)
            filename_dict[name] = value

    print(f"filename_dict len {len(filename_dict)} file_content_dict len {len(file_content_dict)}")
    if len(file_content_dict) != len(filename_dict):
        print("filename not equ file_content")

    if os.path.exists("temp"):
        shutil.rmtree("temp")
    os.mkdir("temp")

    for filename, file_content in filename_dict.items():
        with open(os.path.join("temp", filename), mode="+wb") as f:
            if file_content in file_content_dict:
                for x in file_content_dict[file_content].split(","):
                    f.write(int(x.strip(), 16).to_bytes())
            else:
                print("filename not have file_content")

if __name__ == '__main__':
    main()
