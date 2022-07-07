
import requests
from beebotte import *


_accesskey  = "49VqJ9vAGYrvFlqgILiSLeDN"
_secretkey  = "KUhmrP1mm2w57tVVvSUYf6tPqN2Tu5J9"
_hostname   = 'api.beebotte.com'
bbt = BBT( _accesskey, _secretkey, hostname = _hostname)


bbt.write('Arduino','led',True)

import streamlit as st
st.title('Lights Control')
lit= st.select_slider('Lights',     options=['OFF','ON'])
if lit=='ON':
	bbt.write('Arduino','led',True)
elif lit=='OFF':
	bbt.write('Arduino','led',False)
