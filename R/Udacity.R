# Udacity Project 2 - Bikeshare

## Load lubridate package
install.packages("lubridate")

# Load essential libraries
require(ggplot2)
require(lubridate)
require(RColorBrewer)

## Load the data of our 3 files for each city into workspace
wash <- read.csv("~/Project 2/washington.csv", header = TRUE)
ny <- read.csv("~/Project 2/new-york-city.csv", header = TRUE)
chi <- read.csv("~/Project 2/chicago.csv", header = TRUE)

# Get sense of the data by exploring first rows using head function
head(wash)
head(ny)  # include gender and birth year column
head(chic) # include gender and birth year column

# Add a NA data for washington data so that all cites have same no.of variables
wash[,c("Gender","Birth.Year")] <- NA

names(wash) # to confirm the new columns are added

# Add city column for each table (total of 10 variables:original 9 +City column)
wash[,"City"] <- "Washington"
ny[,"City"] <- "New York"
chi[,"City"] <- "Chicago"

# New data with all three cities
wnc <- rbind(wash, ny, chi)


### Question 1: Explore most common hour a bike is rented
# Extract the hour from our data
dates <- as.POSIXlt(wnc$Start.Time)
hours <- as.data.frame(hour(dates)) # extracting hour
wnc2 <- wnc
ny2 <- ny
wash2 <- wash
chi2 <- chi
wnc2[,"Hour"] <- hours # Add new column hours

# Plot the hour of the day when a bike is rented in each day
hour_graph <- function(data, title){
ggplot(aes(x= Hour),data = data)+
  geom_histogram(aes(y= ..count..), binwidth = 1, col = 'black', fill = "light blue")+
  ggtitle(title)+
  ylab('Count of Bikes Rented')+
  scale_x_continuous(limits = c(0,24),breaks= seq(0,24,2))}

# Most common hour of the day a bike is rented in all 3 cities
hour_graph(wnc2,'Histogram of Days Hours a bike is rented in \n Newyork, Washinghton and Chicago')

# Descriptive statistics:
boxplot(wnc2$Hour, horizontal = TRUE)
summary(wnc2$Hour)
# Numeric variable by using sort function on a table
a1 <- sort(table(wnc2$Hour),decreasing = TRUE) # Sorted table of count of times a bike is hired in each hour
head(a1, 1) # most common hour of the day a bike is rented

# Plot the hour of the day when a bike is rented in each day for each city
hour_graph(wnc2,'Histogram of Days Hours a bike is rented in \n Newyork, Washinghton and Chicago')+
  facet_wrap(~ City)

#Desciptive statistics
by(wnc2$Hour, wnc$City, summary)
ggplot(aes(x=City, y=Hour), data = wnc2)+
  geom_boxplot()



### Question 2: Most common month a bike is rented
m <- as.data.frame(month(dates)) # extracting the day
wnc2[,"Month"] <- m # Add new column for month

old <- c('1', '2', '3', '4', '5', '6')
new <- c('January', 'Febraury', 'March', 'April', 'May', 'June')


wnc2$Month[wnc2$Month %in% old] <- new[match(wnc2$Month,old, nomatch =0 )]

# Month graph function
month_graph <- function(data, title){
ggplot(aes(x= Month, y = ..count..),data = data)+
  geom_bar(fill = "Light green", col = 'black')+
  ggtitle(title)+
  ylab('Count of Bikes Rented')
  }

# Plot the month when a bike is rented in first 6 months of 2017
month_graph(wnc2, 'Barplot of Months a bike is rented in 2017 \n in NewYork, Washinghton and Chicago')


#Desciptive statistics
calculate_mode <- function(x) {
  uniqx <- unique(na.omit(x))
  uniqx[which.max(tabulate(match(x, uniqx)))]
}
calculate_mode(wnc2$Month) # June is the most common month of first 6 months in 2017

# Same plot for each city of the three cities
month_graph(wnc2, 'Barplot of Months a bike is rented in 2017 \n in NewYork, Washinghton and Chicago')+
  facet_grid(.~ City)


### Question 3 : Most common start station
calculate_mode <- function(x) {
  uniqx <- unique(na.omit(x))
  uniqx[which.max(tabulate(match(x, uniqx)))]
}
calculate_mode(wnc$Start.Station)


#### Question 4: compare between travel duration and gender in NY and chicago

# Replace blank cells with na
chi$Gender[chi$Gender == ""]  <-'0'
ny$Gender[ny$Gender == ""] <- '0'

gender_duration <- function(data, title){
  ggplot(aes(x= Gender, y= Trip.Duration/60), data = data)+
  geom_boxplot()+
    ggtitle(title)+
    xlab("Gender")+
    ylab("Trip Duration (min)")+
    coord_cartesian(ylim = c(0,30))}

# For Chicago : Females have trip duration longer than males
gender_duration(subset(chi, !is.na(Gender)),"Box plot of Chicago gender vs Trip duration(min)")
by(chi$Trip.Duration/60, chi$Gender, summary)  
# mean and median not equal .. not normally distributed data .. median is more representative for this data than mean

# For New York :Females have trip duration longer than males
gender_duration(subset(ny, !is.na(Gender)),"Box plot of New York gender vs Trip duration(min)")
by(ny$Trip.Duration/60, ny$Gender, summary) 
