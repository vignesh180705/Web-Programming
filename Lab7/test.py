data=cars
data
summary(data)
v1=var(data[1])
v2=var(data[2])
c=cov(data[1],data[2])
r=c/(sqrt(v1)*sqrt(v2))
r

regression1 = lm(data$speed~data$dist)
regression1

data2 = mtcars
data2

x1=data2$drat
x2=data2$wt
regression2 = lm(data2$hp~x1+x2)
regression2

covariance = cov(data$speed,data$dist)
covariance
plot(data$dist, data$speed)
abline(lm(data$speed~data$dist))
summary(regression1)

cor.test(data$speed, data$dist, method="pearson")
cor.test(data$speed, data$dist, method="spearman")

x=c(15,26,27,25,25.5,27,32,18,22,20,26,24)
y=c(13.35,16.12,16.74,16,13.59,15.73,15.65,13.85,16.07,12.8,13.65,14.42)
regression3 = lm(y~x)
regression3
plot(x,y)
abline(lm(y~x))