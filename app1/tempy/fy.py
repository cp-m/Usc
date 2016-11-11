from django.utils.safestring import mark_safe

def pager():
    page_html = []
    first_html = "<a href='/fy/%d'>首页</a>" %(1,)
    page_html.append(first_html)
    if page <= 1:
        prev_html = "<a href='#'></a>"
    else:
        prev_html = "<a href='/fy/%d'>上一页</a>" % (page-1,)

    for i in range(all_page_count):
        if page == i+1:
            a_hhtml=