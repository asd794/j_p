#!/bin/bash

ps -A|grep bash|sed '1d' |sed s/[[:space:]]//g 


