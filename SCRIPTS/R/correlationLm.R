###correlation###
#lcid
plot(LCID~LCID_daily_percent, data = lcid_stock_data)
cor(lcid_stock_data$LCID, lcid_stock_data$LCID_daily_percent)
#NVDA
plot(NVDA~NVDA_daily_percent, data = nvda_stock_data)
cor(nvda_stock_data$NVDA, nvda_stock_data$NVDA_daily_percent)
###Regression###
lcidmod1<-lm(LCID_daily_percent~LCID,data=lcid_stock_data)
summary(lcidmod1)
nvdamod1<-lm(NVDA_daily_percent~NVDA,data=nvda_stock_data)
summary(nvdamod1)
