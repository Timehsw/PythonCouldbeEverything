# -*- coding: utf-8 -*-
"""
Created by HuShiwei on 2016/11/29 0029.
"""
import random
import datetime
class makeStoreBaseInfo(object):
    def __init__(self):
        self.store_name=['安踏','特步','新百伦','耐克','阿迪','贵人鸟','乔丹','苏菲小店',
                         'MM小店','秋水衣人','百衣百顺','朴坊','锦衣堂',
                         '青苹果','特别特','一房公社','流行坊']
        self.location_city=['北京','上海','广州','贵州','云南','宁夏','武汉','南昌','南京',
                            '杭州','天津','黑龙江','沈阳','赤壁','山西','深圳',
                            '仙桃','荆门','丽江','西藏']
        self.tmall=[0,1]
        self.store={}
        self.storeID=[]

    # 店铺基础信息
    def sample_storeIDAndName(self):
        store={}
        storeID=str(random.randint(20000,80000))
        storeName=random.sample(self.store_name,1)[0]
        if storeID is not self.store.keys():
            self.store[storeID]=storeName
            self.storeID.append(storeID)
            store[storeID]=storeName

        return store

    def sample_tmall(self):
        return random.sample(self.tmall,1)[0]

    def sample_localtion(self):
        return random.sample(self.location_city,1)[0]

    def sample_storeData(self,count=3):
        while count>1:
            isTmall=self.sample_tmall()
            localtion=self.sample_localtion()
            store=self.sample_storeIDAndName()
            for k in store.keys():
                msg="{k} {v} {isTmall} {localtion}".format(k=k,v=store[k],isTmall=isTmall,localtion=localtion)
                # print msg
            count=count-1

    # 店铺信用
    def sample_sellerCredit(self):
        return random.randint(1,5)

    def sample_goodsScore(self):
        return random.randint(1,5)

    def sample_serviceScore(self):
        return random.randint(1,5)

    def sample_speedScore(self):
        return random.randint(1,5)

    def sample_updateDataInfo(self):
        year=str(random.randint(2013,2016))
        month=str(random.randint(1,11))
        day=str(random.randint(1,28))
        hour=str(random.randint(0,23))
        min=str(random.randint(0,59))
        second=str(random.randint(0,59))
        uniqueNum=year+month+day+hour+min+second
        return uniqueNum

    def sample_storeScore(self,count=10):
        while count>0:
            storeID=random.sample(self.storeID,1)[0]
            credit=self.sample_sellerCredit()
            goodsScore=self.sample_goodsScore()
            serviceScore=self.sample_serviceScore()
            speedScore=self.sample_speedScore()
            updateData=self.sample_updateDataInfo()
            msg="{storeID} {credit} {goodsScore} {serviceScore} {speedScore} {updateData}".format(storeID=storeID,credit=credit,
                                                                                                  goodsScore=goodsScore,serviceScore=serviceScore,
                                                                                                  speedScore=speedScore,updateData=updateData)
            print msg
            count=count-1






if __name__ == '__main__':


    taobao=makeStoreBaseInfo()
    taobao.sample_storeData(100)
    taobao.sample_storeScore(100)