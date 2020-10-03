#!/usr/bin/env python3

#import i2c_lcd_driver

import os
import lcddriver
from time import sleep
from flask import Flask, jsonify, make_response, request, render_template


#mylcd = i2c_lcd_driver.lcd()

mylcd = lcddriver.lcd()

app = Flask(__name__, template_folder='myTemplate')

def switchTH() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Welcome to", 1)
    mylcd.lcd_display_string("Tom's Hardware!", 2)
    sleep(1)
    
def switchAvailable() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status:Available", 1)
    sleep(1)

def switchBusy() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status: Busy", 1)
    sleep(1)


def switchClass() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status:In class", 1)
    sleep(1)


def switchAway() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status: Away", 1)
    sleep(1) 

    
def switchMeeting() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("In a meeting", 1)
    sleep(1)
    
def switchLabo() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("In the laboratory", 1)
    sleep(1)

def switchClear() :
    mylcd.lcd_clear()
    sleep(1)



@app.route('/api/th', methods=['GET'])
def apiTH() :
    switchTH()
    return jsonify({})
    
# API switchAvailable
@app.route('/api/available', methods=['GET'])
def apiAvailable() :
    switchAvailable()
    return jsonify({})

    
# API Busy
@app.route('/api/busy', methods=['GET'])
def apiBusy() :
    switchBusy()
    return jsonify({})


@app.route('/api/class', methods=['GET'])
def apiClass() :
    switchClass()
    return jsonify({})

    
# API Away
@app.route('/api/away', methods=['GET'])
def apiAway() :
    switchAway()
    return jsonify({})
    
# API switchMeeting
@app.route('/api/meeting', methods=['GET'])
def apiMeeting() :
    switchMeeting()
    return jsonify({})


@app.route('/api/laboratory', methods=['GET'])
def apiLabo() :
    switchLabo()
    return jsonify({})

  
# API clear
@app.route('/api/clear', methods=['GET'])
def apiClear() :
    switchClear()
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@app.route('/')
def index():
    #url_for('html', filename='lcd.html')
    return render_template('web.html')
    
if __name__ == '__main__':
    #app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


