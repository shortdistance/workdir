#Scrapy  tutorial project

# !!! PLEASE SEE 

[https://github.com/qfbot/qfbot](https://github.com/qfbot/qfbot)

### Glance

Install:

    git clone https://github.com/qfboys/qfbot.git
    pip install -r requirements.txt

Usage:

    $cd demo/scrapy_cn
    $scrapy list
    $scrapy crawl onepage

Build with docker:

    $sudo docker build -t addbook/qfbot .
    $sudo docker -rm -t -i addbook/qfbot
    $root@xxxxxx:scrapy

![](https://github.com/addwork/scrapy_cn/blob/master/doc/images/scrapy_docker.jpg?raw=true)

## structure

    scrapy_cn/
        -doc/       ...关于工具插件的使用指南
        -tools/     ...开发中scrapy有用的插件，使用参考doc
        -demo/      ...简单的中文网站抓取爬虫实现
        -crawl/     ...较大规模的爬虫设计以及配置
        -linkbase/  ...Linkbase基础爬虫实现
        -schedule/  ...可调度爬虫的简单实现
        -distrib/   ...分布式负载

## Contact:

- QQ群:282889215  

- blog: [scu.qfboys.com](scu.qfboys.com) 

## Features

- [ ] 开放Linkbase抓取的爬虫
- [x] 开放可管理调度任务的爬虫
- [ ] 大规模任务负载的分布式处理实现
- [ ] 支持mq
- [ ] 将下载与完成与解析任务分离,下载结果直接压入MQ中.
- [ ] 增加解析worker脚本

- [ ] 增加任务查看的统一的API
- [ ] 增加web-api
- [ ] 以及管理API
- [ ] 增加SRP过程

- [ ] 增加站点raw数据压缩，以及HDFS相关处理
- [ ] 爬虫任务调度

## Lisence: BSD Lisence


