# -*- coding: utf-8 -*-
"""
Created by HuShiwei on 2016/11/26 0026.
"""

import random
import time


class WebLogGeneration(object):
    def __init__(self):
        self.user_agent_dist = {
            0.0: "Mozilla/6.0 (compatible; MSIE 8.0; Windows NT7.0)",
            0.1: "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT6.0)",
            0.2: "Mozilla/4.0 (compatible; MSIE 5.0; WindowsNT)",
            0.3: "Mozilla/5.0 (Windows; U; Windows NT 5.1)Gecko/100070309 Firefox/2.0.0.3",
            0.4: "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT5.2)",
            0.5: "Mozilla/5.0 (Windows; U; Windows NT 5.1)Gecko/2007035409 Firefox/2.8.1.3",
            0.6: "Mozilla/5.0 (Windows; U; Windows NT 5.2)AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1Safari/525.13",
            0.7: "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML,like Gecko) Chrome/0.2.149.27 Safari/525.13",
            0.8: "Mozilla/5.0 (iPhone; U; CPU like Mac OS X)AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93Safari/419.3",
            0.9: "Mozilla/5.0 (Windows; U; Windows NT 5.2)AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1Safari/525.13",
            1: ""
        }
        self.ip_slice_list = [10, 45, 21, 34, 65, 68, 132, 156, 134, 126, 156, 178, 159, 178,
                              201, 209, 214, 218, 222]
        self.url_path_list = [
            "login.php",
            "view.php",
            "list.php",
            "upload.php",
            "admin/login.php",
            "edit.php",
            "index.html"
        ]
        self.http_refer_list = [
            "http://www.baidu.com/s?wd={query}",
            "http://www.google.com/search?q={query}",
            "http://www.sogou.com/web?query={query}",
            "http://www.yahoo.com/s?p={query}",
            "http://cn.bing.com/searcg?q={query}",
        ]
        self.search_keyword = ["spark", "hadoop", "storm", "mr",
                               "spark mllib", "spark sql",
                               "java web", "flume", "kafka"]

    def sample_ip(self):
        slice = random.sample(self.ip_slice_list, 4)
        return ".".join([str(item) for item in slice])

    def sample_url(self):
        return random.sample(self.url_path_list, 1)[0]

    def sample_user_agent(self):
        dist_uppon = random.uniform(0, 1)
        return self.user_agent_dist[float('%0.1f' % dist_uppon)]

    def sample_refer(self):
        # 只有20%流量有refer
        if random.uniform(0, 1) > 0.2:
            return "-"
        refer_str = random.sample(self.http_refer_list, 1)
        query_str = random.sample(self.search_keyword, 1)
        return refer_str[0].format(query=query_str[0])

    def sample_one_log(self, count=3):
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        while count > 1:
            query_log = "{ip} - - [{local_time}] \"GET /{url} HTTP/1.1\" 200 0 \"{refer}\" \"{user_agent}\" \"-\"".format(
                ip=self.sample_ip(),
                local_time=time_str, url=self.sample_url(),
                refer=self.sample_refer(), user_agent=self.sample_user_agent())
            print query_log
            count = count - 1


if __name__ == '__main__':
    web_log_gene = WebLogGeneration()
    web_log_gene.sample_one_log(random.uniform(30000,50000))
    #web_log_gene.sample_one_log(random.uniform(100, 300))
