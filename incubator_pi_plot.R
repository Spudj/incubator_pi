##======================================================================
## incubator_pi_plot.R
## Jasen Finch 14/14/2014
## Script to plot Temperature and Humidity outputs from incubator_pi.py
##======================================================================

library(ggplot2)

## Read in Path and filename and data
args<-commandArgs(TRUE)
Path <- args[1]
file <- args[2]
data <- read.csv(paste(Path,file,sep="/"))

## Prep data and plot
names(data)[3:4] <- c("Temperature", "Humidity") 
date <- data$Date
time <- data$Time
int <- sapply(seq(1,length(date)),function(x,a,b){paste(a[x],b[x],sep=" ")},date,time)
date.time <- strptime(int,format="%Y-%m-%d %H:%M:%S")
data$Time <- date.time


file.1 <- gsub(".csv","",file)

jpeg(paste(Path,paste(file.1,"_temp_plot.jpeg",sep=""),sep="/"))
ggplot(data, aes(x=Time, y=Temperature)) + geom_line(color="Blue") + ylab("Temperature (*C)") + ggtitle("Temperature Plot")

jpeg(paste(Path,paste(file.1,"_humidity_plot.jpeg",sep=""),sep="/"))
ggplot(data, aes(x=Time, y=Humidity)) + geom_line(color="Green") + ylab("Humidity (%)") + ggtitle("Humidity Plot")
