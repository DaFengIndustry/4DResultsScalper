# 4DResultsScalper
4D is a type of lottery offered by Singapore pools, I do not endorse gambling play at your own risk. This project aims to obtain winning history of numbers into a analyzable format, this would later go on to proof that 4D is purely random and pass results does not affect future results. 

## Acknowledgement
This project owes special thanks to (https://github.com/nwfxyz/4D_analytics.git) for inspiring this project and providing solution and alternative the scraping the data. 
## Obtaining Data
The data is obtained from (http://www.singaporepools.com.sg/en/product/Pages/4d_cpwn.aspx)
## Results
The counts of each digit's appearance can be found using the DigitAppearance.py which proofs that all digits have equal odds of happening. DigitPairAppearance.py hopes to find 2 numbers that always appear together in winning tickets regardless of position and proofs that all 2 different numbers pair together gave equal odds of winning. 
## About
4DscraperV1.py attempts to use webscrapping techniques with selenium to scalp the data from the website but ultimately failed, if you want to scalp the latest data from 1986 to the latest results when you are scalping use 4DscraperV2.py which is inspired by 4D_analytics.git which calls the API directly to obtain the data. Results from the csv contains results from 1986 to 9/11/2025. 
 

