# EduTech-Task11-Customer-Segmentation analysis

## Tools Used
Python, Pandas, Scikit-learn, Matplotlib, Seaborn

## Dataset
Mall Customers Dataset (Kaggle)
Link: https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

## Analysis Performed
1. RFM-style analysis using Age, Annual Income, Spending Score
2. Feature Scaling using StandardScaler
3. Elbow Method to find optimal K
4. K-Means Clustering (K=5)
5. Cluster visualization and segment profiling

## Segments Found
- Cluster 0: Low income, Low spending
- Cluster 1: High income, High spending (Premium customers)
- Cluster 2: Low income, High spending
- Cluster 3: High income, Low spending
- Cluster 4: Average income, Average spending

## Interview Answers
**What is RFM?**
RFM stands for Recency, Frequency, Monetary:
- Recency: Customer ne kitne time pehle purchase kiya
- Frequency: Kitni baar purchase kiya
- Monetary: Kitna paisa kharch kiya
RFM se customers ko valuable aur non-valuable segments mein divide karte hain.

**Value of segmentation?**
Customer segmentation se companies targeted marketing kar sakti hain. Har segment ke liye alag strategy banate hain - jaise premium customers ko exclusive offers dena, low spenders ko discounts dena. Isse marketing cost kam hoti hai aur ROI badhta hai.
