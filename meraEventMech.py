#done
import mechanize
import cookielib

def trovitjob(form):
  return form.attrs.get('id', None) == 'loginform'

def step1(form):
  return form.attrs.get('id', None) == 'step1'

def step2(form):
  return form.attrs.get('id', None) == 'step2'

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Chrome')]
br.open('http://www.meraevents.com/Login')
br.select_form('fSignIn')
br['UserNmae'] = "sharad.shubham@gmail.com"
br['UPassword'] = "dendidendi"
br.submit()
br.open('http://www.meraevents.com/dashboard-account')
br.open(br.click_link(text = 'Create Event'))
br.select_form('form2')
br['eventtype'] = ['NoReg']
br['event_title'] = 'Tes tEven tFo rTestin g'
br['event_url'] = 'Tes tEven tFo rTestin g'


