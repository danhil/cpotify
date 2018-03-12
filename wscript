#! /usr/bin/env python
# encoding: utf-8

VERSION='0.0.0'
APPNAME='cpotify'

top = '.'
out = 'build'

def options(opt):
    opt.load('compiler_cxx')
    opt.recurse(['proto'])

def configure(conf):
    conf.load('compiler_cxx')
    conf.recurse(['proto'])

def build(bld):
    bld.recurse(['proto'])
