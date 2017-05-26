from utils.log import log


def parse_dcusers():
    users = []
    wx_users = []
    with open('data/4.csv', 'r', encoding='gbk') as f:
        for i in f.readlines():
            if len(i.split(',')) == 1:
                userid = i.split(',')[0].split('\n')[0]
                username = '空'
            else:
                userid = i.split(',')[1].split('\n')[0]
                username = i.split(',')[0]
            if len(userid) == 7:
                userid = '0' + userid
            if userid[:2] == '99':
                wx_users.append((userid, username))
            else:
                users.append((userid, username))
    return users, wx_users


def parse_hrusers():
    hr_users = []
    with open('data/crv1.csv', 'r', encoding='gbk') as f:
        for i in f.readlines():
            username = i.split(',')[22].replace('"', '')
            userid = i.split(',')[23].replace('"', '')
            hr_users.append((userid, username))
    return hr_users


def cmp_users():
    diff_users = []
    dc_users = parse_dcusers()[0]
    hr_users = parse_hrusers()
    hl = []
    for huser in hr_users:
        hl.append(huser[1])
    for duser in dc_users:
        if duser[0] in hl:
                pass
        else:
            diff_users.append((duser[0], duser[1]))
    return diff_users


if __name__ == '__main__':
    wx_users = parse_dcusers()[1]
    log('外协人员信息----')
    log('        ')
    for user in wx_users:
        log(user)
    log('在域中但不在HR中人员信息----')
    log('        ')
    di_users = cmp_users()
    for di in sorted(di_users):
        log(di)
