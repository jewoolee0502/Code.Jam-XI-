# Code.Jam-XI-

Broadsign challenge 

**Theme:**
- Leverage big data and machine learning to forecast an advertising campaign’s reach.

**Description:**

Out of home advertising is increasingly digital. Electronic screens are taking precedence over static billboards due to the speed at which they can adapt their content to the audience around them.

One of the goals of DOOH (digital out of home) campaign planning tools is to predict the number of impressions (i.e. the number of times an ad was viewed) that a given campaign will receive. This helps advertisers iterate through campaign proposals and evaluate which will yield the best results.

Forecasting impressions is challenging because a campaign can potentially target tens of thousands of screens, each with their own audience and pattern of impressions. And because clients expect a responsive experience as they adjust and fine tune their campaign, these predictions need to be computed quickly.

Your challenge is to implement a web API that can quickly forecast the number of impressions that a campaign will receive. Your solution will be evaluated on its performance and accuracy, along with the sophistication of your design.


**Technical description:**

At the start of the competition you will be provided with historical impression data on which to base your solution. Each row of data contains the number of impressions for a screen for a specific hour, along with some additional information (which you may or may not find pertinent to your solution).

Your API will receive a payload representing a campaign and will have to return a prediction for the number of impressions it will receive. For simplicity, we will assume that every campaign is exactly one week in duration. A campaign consists of a list of screen ids and a schedule, which is a list of hours during the week at which the campaign should play. The schema for the payload is
{
  "screens": [<list of screen ids>],
  "schedule": [
    "Mon-00", // Monday at midnight
    "Mon-01", // Monday at 1 am
    "Tue-13", // Tuesday at 1pm
    ...
  ]
}
In general, a campaign can contain thousands of screens and play at arbitrary hours of the week.

To evaluate the accuracy of your forecast, we will use actual campaigns and compare their true impression count to your predictions.

You should aim for a response time of under 100ms, but slower isn’t necessarily a problem if you can compensate by having greater accuracy.

You have the liberty to take any approach you wish. However, we do encourage you to consider leveraging some of the many data mining and machine learning techniques and libraries that are available. These include pandas for data exploration and analysis, scikit-learn for machine learning models, and Jupyter notebook for rapid prototyping.
