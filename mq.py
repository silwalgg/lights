
import requests
from beebotte import *

import streamlit as st
_accesskey  = "49VqJ9vAGYrvFlqgILiSLeDN"
_secretkey  = "KUhmrP1mm2w57tVVvSUYf6tPqN2Tu5J9"
_hostname   = 'api.beebotte.com'
bbt = BBT( _accesskey, _secretkey, hostname = _hostname)

records = bbt.read('Arduino','led',limit = 5)
if records[0]['data']:
	value='ON'
else:
	value='OFF'



st.title('Lights Control')
lit= st.select_slider('Lights',     options=['OFF','ON'],value=value)
if lit=='ON':
	bbt.write('Arduino','led',True)
elif lit=='OFF':
	bbt.write('Arduino','led',False)
#hello
