from lib.ColoredObject import Color

#url_regex = ['((http|https)\:\/\/)?([a-zA-Z0-9\.\/\?\:@\-_=#]+\.(com|net|org|co|us|ru|gov|edu|info))([a-zA-Z0-9\.\&\/\?\:@\-_=#])*']
#path_regex = ['(\/[^\/]+){0,2}\/?']

subdomain_regex = lambda subdomain: '(.*\.)?{}(\.)?'.format(subdomain)

dom_sources_regex = [
'document.url',
'document.documenturi',
'Document.URLUnencoded',
'Document.baseURI',
'Location.href',
'Location.search',
'Location.hash',
'Location.pathname',
'Document.cookie',
'Document.referrer',
'Window.name',
'History.pushState',
'History.replaceState',
'LocalStorage',
'SessionStorage',
'window.location',
'document.location'
]

dom_sinks_regex = [
'eval',
'setTimeout',
'setInterval',
'setImmediate',
'execScript',
'cyrpto.generateCRMFRequest',
'ScriptElement',
'ScriptElement.src',
'ScriptElement.text',
'ScriptElement.textContent',
'ScriptElement.innerText',
'document.write',
'document.writeln'
]

others_regex = [
'API',
'key',
'secretKey'
]

#add 0-9 in regex
web_services_regex = [
'([a-zA-Z-.]*s3[a-zA-Z-.]*\.?amazonaws\.com\/?[a-zA-Z-.]*)',
'([a-zA-Z-.]*?storage\.googleapis\.com\/?[a-zA-Z-.]*)',
'([a-zA-Z-.]*?digitaloceanspaces\.com\/?[a-zA-Z-.]*)',
'([a-zA-Z-.]*?blob\.core\.windows\.net\/?[a-zA-Z-.]*)'
]

skip_js_regex = [
'.*jquery.*'
]

ColorObj = Color()
