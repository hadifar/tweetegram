# -*- coding: utf-8 -*-
#
# Copyright 2018 Amir Hadifar. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from tweepy import OAuthHandler
from tweepy import Stream

from app import config
from app.listener import Listener

if __name__ == '__main__':

    listener = Listener()
    auth = OAuthHandler(config.API_KEY, config.API_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, listener)
    # if you want to stream specific user time-line
    # find his/her ID with following website and
    # replace his/her twitter ID with mine
    # http: // mytwitterid.com /
    stream.filter(follow=['2578395857'])  # mine
    # stream.filter(track=['google'])   # fermat
