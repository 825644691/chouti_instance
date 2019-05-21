class PagerHelper:
    def __init__(self, total_count, current_page, base_url, number):
        self.current_page = current_page
        self.total_count = total_count
        self.number = int(number)
        self.base_url = base_url

    @property
    def page_start(self):
        return (self.current_page-1) * self.number

    @property
    def page_end(self):
        return self.current_page*self.number

    def pager_str(self):
        v, a = divmod(self.total_count, self.number)
        if a != 0:
            v += 1
        pager_list = []
        if v <= 11:
            page_range_start = 1
            page_range_end = v + 1
        else:
            if self.current_page <= 6:
                page_range_start = 1
                page_range_end = 12
            else:
                page_range_start = self.current_page - 5
                page_range_end = self.current_page + 5 + 1
                if page_range_end > v:
                    page_range_end = v + 1
        if self.current_page == 1:
            pager_list.append("<a href='javascript:void(0);'>上一页</a>")
        else:
            pager_list.append("<a href='%s?p=%s'>上一页</a>" % (self.base_url, self.current_page - 1))
        for i in range(page_range_start, page_range_end):
            if i == self.current_page:
                pager_list.append("<a class='active' href='%s?p=%s'>%s</a>" % (self.base_url, i, i))
            else:
                pager_list.append("<a href='%s?p=%s'>%s</a>" % (self.base_url, i, i))
        if self.current_page == v:
            pager_list.append("<a href='javascript:void(0);'>下一页</a>")
        else:
            pager_list.append("<a href='%s?p=%s'>下一页</a>" % (self.base_url, self.current_page + 1))
        pager = "".join(pager_list)
        return pager
