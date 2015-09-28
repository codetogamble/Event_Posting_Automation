import mechanize
import cookielib

def event_form(form):
   return form.attrs.get('id', None) == 'event_form'

def newjob(form):
  return form.attrs.get('id', None) == 'newjob'

def login_auth(form):
  return form.attrs.get('id', None) == 'form-openid'

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

   #br.set_debug_http(True)
   #br.set_debug_responses(True)
   # Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Chrome')]
br.open('https://www.eventbrite.com/login/')
br.select_form(nr = 1)
br['email'] = 'saranya@venturesity.com'
br['password'] = 'Venturesity@123'
br.submit()
br.open('https://www.eventbrite.com/create')
br.select_form(predicate = event_form)
br.set_all_readonly(False)
br.set_value('js-dtp-datepicker-input date hasDatepicker',nr = 0)
br.set_value('js-dtp-timepicker-input time form__input--xshort js-timepicker-input',nr = 1)
br.set_value('js-dtp-datepicker-input date hasDatepicker',nr = 2)
br.set_value('js-dtp-timepicker-input time form__input--xshort js-timepicker-input',nr = 3)
for x in br.controls:
	print x.id
br['group-details-name'] = 'test event'
br['group-location-venue'] = 'CVB'
br['group-location-address_1'] = 'CVB'
br['group-location-address_2'] = 'BNM'
br['group-location-city'] = 'Bangalore'
br['group-location-state'] = 'Karnataka'
br['group-location-postal_code'] = '560018'
br['group-location-country'] = 'India'
br.controls[0] = '10/01/2015' 
br.controls[1] = '07:00pm'
br.controls[2] = '10/01/2015'
br.controls[3] = '10:00pm'
#br['group-tickets-0-ticket_type'] = 'RSVP'
#br['group-tickets-0-quantity_total'] = str(100)


