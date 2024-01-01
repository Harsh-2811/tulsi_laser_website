import urllib.request
import time	
#lst=['mech1.jpg','procedures-arrow.png','mech2.jpg','proj1.jpg','mech3.jpg','proj2.jpg','member1.jpg','proj3.jpg','member2.jpg','proj4.jpg','member3.jpg','proj5.jpg','member4.jpg','proj6.jpg','mob-menu.png','proj7.jpg','navi-plus.png','quote.jpg','news-big1.jpg',
#lst=['service-two-img1.jpg','news-big2.jpg','service-two-img2.jpg','news-big3.jpg','service-two-img3.jpg','news-dr1.jpg','services-img1.jpg','news-dr2.jpg','services-img2.jpg','news-img1.jpg','services-img3.jpg','news-img2.jpg','services-img4.jpg','news-img3.jpg','shop-thumbnail.jpg','news-img4.jpg','shop-thumbnail2.jpg','news-img5.jpg','shop-thumbnail3.jpg','news-thumb1.jpg','shop1.jpg','news-thumb2.jpg','shop2.jpg','news-thumb3.jpg','shop3.jpg','news-thumb4.jpg',
lst=['news-thumb5.jpg','sub-banner.jpg','news-thumb6.jpg','team%20work.png','news1.jpg','test1.jpg','news2.jpg','test2.jpg','news3.jpg','test3.jpg','pages-header.jpg','test4.jpg','paging-arrow.png','test5.jpg','pajpall.jpg','test6.jpg','petroleum1.jpg','testimonial-bg.jpg','petroleum2.jpg','time-icon-bg.png','power1.jpg','white-arrows.jpg','power2.jpg','worker.png','procedures-arrow-hover.png']
for i in lst:
	time.sleep(1)
	print(i)
	urllib.request.urlretrieve("http://lazeapostolski.com/industry/images/"+i, i)