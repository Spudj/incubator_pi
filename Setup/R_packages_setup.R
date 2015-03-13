##====================================================##
## R_packages_setup.R
## Jasen Finch 25-05-2014
## Setup R for use with incubator_pi
##====================================================##

print("Installing Rcpp...")
install.packages("~/Documents/incubator_pi/R_packages/Rcpp_0.10.5.tar.gz",repos=NULL,type="source")
print("Installing plyr...")
install.packages("~/Documents/incubator_pi/R_packages/plyr_1.8.tar.gz",repos=NULL,type="source")
print("Installing lattice...")
install.packages("lattice",repos="http://www.stats.bris.ac.uk/R/")
print("Installing reshape2...")
install.packages("~/Documents/incubator_pi/R_packages/reshape2_1.2.tar.gz",repos=NULL,type="source")
print("Installing MASS...")
install.packages("~/Documents/incubator_pi/R_packages/MASS_7.3-23.tar.gz",repos=NULL,type="source")
print("Installing ggplot2...")
install.packages("~/Documents/incubator_pi/R_packages/ggplot2_0.9.3.1.tar.gz",repos=NULL,type="source")