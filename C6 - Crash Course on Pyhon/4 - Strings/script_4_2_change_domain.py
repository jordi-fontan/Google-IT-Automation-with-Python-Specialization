# replace old domains in a list of domains
old_domain='gmail.com'
new_domain='gmail.es'
def replace_domain(mail):
    if ('@'+ old_domain) in mail:
        index= mail.index('@')
        new_mail= mail[:index]+'@'+new_domain
        print(new_mail,'<-----',mail)
        return new_mail

    else:
        print('No Changes for',mail)
        return mail    
replace_domain('jojo@ttt.lo')

replace_domain('lolito@gmail.com')
replace_domain('alibaba@gmail.com')
replace_domain('vovo@gmail.nz')

# [Running] python -u "c:\sharedData\projects\edu\CB-PhyDS\replaceOldDomains.py"#
# No Changes for jojo@ttt.lo
# lolito@gmail.es <----- lolito@gmail.com
# alibaba@gmail.es <----- alibaba@gmail.com
# No Changes for vovo@gmail.nz

# [Done] exited with code=0 in 0.323 seconds
