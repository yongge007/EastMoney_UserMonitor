# EastMoney_UserMonitor（东财贴吧用户发帖/回帖跟踪脚本）


https://caifuhao.eastmoney.com/gbapi/AuthorCFHList?listName=web&ps=6&p=1&uid=4490346040458668
<!-- "post_source_id": "20241129165900633511510", -->

长文详情：https://caifuhao.eastmoney.com/news/20241129165900633511510
<script>
  try {
    var extenddata= {"ArtCode":"20241129165900633511510","SubTitle":"","ColumnIds":"2","SubColumnIds":"","ListImage":"","Digest":"","MediaName":"","MediaType":"","RelationAccountId":"","IsLink":0,"IsSimpleVideo":0,"Videos":[],"TipState":1,"ArticleStocks":["zssh000001"],"Participles":[],"CategoryId":"","TagId":"0","ArticleType":0,"Voices":[],"DigestAuto":"$上证指数(SH000001)$      昨天说了点技术。不好保留。所以删了。你们有自己的意见可以保留。不需要在我帖子下面说。我发出来是给信任我的看的。你不信我我说了反着来就行了。比如那些还在等3100的。2800的。其实炒股就是做好自己。炒股就是要自信。既然自己相信会到3100那么一定要等到3100。也别和我杠，要杠的把我1月15号大盘开始调整后发的帖子评论看完。今天收了3326。我只能说，控的太好了。昨天说了大盘应该会在3275-3330之间玩个2天。今天拉到了我前几天给的诱多点3350以","IsOriginal":0,"MisdeedState":0,"MisdeedReason":"","ApprovalState":1,"ApprovalReason":"","TimingPost":0,"TimingPostTime":"","LastModifyFrom":null,"GubaTalkCategoryId":null,"GubaTalkId":null,"GubaTalkVersion":null,"CFHQuote":null,"CatalogPattern":0,"ImportState":0,"IsReCommendRead":0,"ZMTBizType":0,"ZMTLKType":0,"ZMTLKVideoID":null,"ZMTLKVideoState":0,"ZMTLKVideoUIStyle":0,"ZMTLKVideoPubState":0,"ZMTLKStartTime":null,"ZMTLKEndTime":null,"ZMTLKCover":null,"ZMTLKHCover":null,"ZMTLKVCover":null,"ZMTLKHotScore":0,"ZMTLKHotScoreSwitch":false,"ZMTLKWebDistType":0,"ZMTPlatFrom":null,"ZMTLKAppDistType":0,"ZMTLKMpParam":null,"ZMTLKExt":null,"ZMTLKSource":0,"ZMTLKColumnName":null,"ZMTLKSubColumnName":null,"ZMTLKListState":0,"ZMTLKVodWith":0,"ZMTLKVodHigh":0,"ZMTVideoLabel":null,"ZMTRecVideoID":null,"ZMTStocks":null,"ZMTJJZhCode":null,"ZMTActType":0,"ZMTActStartTime":null,"ZMTActEndTime":null,"ZMTOmsPlat":0,"ArticleStocksList":[{"StockID":"zssh000001","StockName":"上证指数"}],"postmodules":[]}
    var articleTxt = "<div class=\"xeditor_content app_h5_article\"><p><span class=\"insert-data guba_stock\" data-marketcode=\"SH000001\" data-markettype=\"1\" data-stockcode=\"000001\" data-stockname=\"上证指数\" data-dougu=\"0\">$上证指数(SH000001)$&nbsp;</span>&nbsp;</p><p>昨天说了点技术。</p><p>不好保留。</p><p>所以删了。</p><p>你们有自己的意见可以保留。</p><p>不需要在我帖子下面说。</p><p>我发出来是给信任我的看的。</p><p>你不信我我说了反着来就行了。</p><p>比如那些还在等3100的。2800的。</p><p>其实炒股就是做好自己。</p><p>炒股就是要自信。</p><p>既然自己相信会到3100那么一定要等到3100。</p><p>也别和我杠，要杠的把我1月15号大盘开始调整后发的帖子评论看完。</p><p>今天收了3326。我只能说，控的太好了。</p><p>昨天说了大盘应该会在3275-3330之间玩个2天。</p><p>今天拉到了我前几天给的诱多点3350以上。</p><p>也算是个小诱多。</p><p>不过这个没多大回踩。</p><p>下周呢很简单。</p><p>下周一连续强势今天就直接站上了3340以上了。</p><p>既然今天回落了。并且回落到我给的空间3330以内。</p><p>那么就一切照旧。</p><p>下周还是走线为主。</p><p>有个超级诱多还没来。</p><p>下周如果周1-2走的很墨迹。那么要注意周3-4出现一波跌。周五给大阳。</p><p>周一如果给阳线，但是有冲高回落收红但是不强，那么要小心周二出现阴线。</p><p>说真的。我都很懒的具体去看。</p><p>大趋势把握住就行了。短期涨跌真的不符合我的操作。</p><p>就这样，周末快乐。</p><p>时间也很快。一下就12月了。</p></div>"
  } catch (error) {
    
  }
</script>

## Crontab 设置

```bash
*/3 * * * * nohup ~/anaconda3/bin/python ~/Documents/Workspace/github/eastmoney_monitor/my_reply.py >> ~/reply.log 2>&1 &
*/3 * * * * nohup ~/anaconda3/bin/python ~/Documents/Workspace/github/eastmoney_monitor/my_post.py >> ~/post.log 2>&1 &
```