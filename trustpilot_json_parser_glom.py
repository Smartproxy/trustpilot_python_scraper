import json
import requests
from bs4 import BeautifulSoup
from glom import glom


url = "https://scrape.smartproxy.com/v1/tasks?universal="

payload = {
    "target": "universal",
    "url": "https://www.trustpilot.com/review/panaceafinancial.com",
    "headless": "html",
    "device_type": "desktop"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic AUTH"
}

def main():

    response = requests.post(url, json=payload, headers=headers)

    json_data = response.text

    parsed_data = json.loads(json_data)

    content = parsed_data['results'][0]['content']

    soup = BeautifulSoup(content, "html.parser")

    # Find the script tag with id "__NEXT_DATA__"
    data_script = soup.select_one('script#__NEXT_DATA__')

    # Extract the contents of the script tag
    data_string = data_script.text

    data = json.loads(data_string)

    # You can access the object data here
    pageUrl = glom(data, 'props.pageProps.pageUrl')
    businessUnit = glom(data, 'props.pageProps.businessUnit')
    displayName = glom(businessUnit, 'displayName')
    identifyingName = glom(businessUnit, 'identifyingName')
    trustScore = glom(businessUnit, 'trustScore')
    websiteTitle = glom(businessUnit, 'websiteTitle')
    profileImageUrl = glom(businessUnit, 'profileImageUrl')
    stars = glom(businessUnit, 'stars')
    categoryName = glom(businessUnit, 'categories.0.name')
    categoryId = glom(businessUnit, 'categories.0.id')
    categoryRank = glom(businessUnit, 'categories.0.rank')
    topLevelDisplayName = glom(businessUnit, 'breadcrumb.topLevelDisplayName')
    locationsCount = glom(businessUnit, 'locationsCount')
    isClosed = glom(businessUnit, 'isClosed')
    isCollectingReviews = glom(businessUnit, 'isCollectingReviews')
    verifiedByGoogle = glom(businessUnit, 'verification.verifiedByGoogle')
    verifiedBusiness = glom(businessUnit, 'verification.verifiedBusiness')
    verifiedPaymentMethod = glom(businessUnit, 'verification.verifiedPaymentMethod')
    hasCollectedIncentivisedReviews = glom(businessUnit, 'hasCollectedIncentivisedReviews')
    email = glom(businessUnit, 'contactInfo.email')
    address = glom(businessUnit, 'contactInfo.address')
    city = glom(businessUnit, 'contactInfo.city')
    country = glom(businessUnit, 'contactInfo.country')
    phone = glom(businessUnit, 'contactInfo.phone')
    zipCode = glom(businessUnit, 'contactInfo.zipCode')
    isUsingPaidFeatures = glom(businessUnit, 'activity.isUsingPaidFeatures')
    hasSubscription = glom(businessUnit, 'activity.hasSubscription')
    isAskingForReviews = glom(businessUnit, 'activity.isAskingForReviews')
    claimedDate = glom(businessUnit, 'activity.claimedDate')
    averageDaysToReply = glom(businessUnit, 'activity.replyBehavior.averageDaysToReply')
    lastReplyToNegativeReview = glom(businessUnit, 'activity.replyBehavior.lastReplyToNegativeReview')
    negativeReviewsWithRepliesCount = glom(businessUnit, 'activity.replyBehavior.negativeReviewsWithRepliesCount')
    replyPercentage = glom(businessUnit, 'activity.replyBehavior.replyPercentage')
    totalNegativeReviewsCount = glom(businessUnit, 'activity.replyBehavior.totalNegativeReviewsCount')
    reviews = glom(data, 'props.pageProps.reviews')
    filters = glom(data, 'props.pageProps.filters')
    totalNumberOfReviews = glom(filters, 'totalNumberOfReviews')
    totalNumberOfFilteredReviews = glom(filters, 'totalNumberOfFilteredReviews')
    currentPage = glom(filters,'pagination.currentPage')
    perPage = glom(filters,'pagination.perPage')
    totalCount = glom(filters, 'pagination.totalCount')
    totalPages = glom(filters, 'pagination.totalPages')
    ratingsTotal = glom(filters, 'reviewStatistics.ratings.total')
    ratingsOneStar = glom(filters, 'reviewStatistics.ratings.one')
    ratingsTwoStar = glom(filters, 'reviewStatistics.ratings.two')
    ratingsThreeStar = glom(filters, 'reviewStatistics.ratings.three')
    ratingsFourStar = glom(filters, 'reviewStatistics.ratings.four')
    ratingsFiveStar = glom(filters, 'reviewStatistics.ratings.five')




    # Create a dictionary
    page_info = {  
        'PageURL': pageUrl,
        'DisplayName': displayName,
        'IdentifyingName':identifyingName,
        'TrustScore': trustScore,
        'WebsiteTitle': websiteTitle,
        'ProfileImageURL': profileImageUrl,
        'Stars': stars,
        'CategoryName': categoryName,
        'CategoryID': categoryId,
        'CategoryRank': categoryRank,
        'TopLevelDisplayName': topLevelDisplayName,
        'NumberOfLocations': locationsCount,
        'IsClosed': isClosed,
        'IsCollectingReviews': isCollectingReviews,
        'VerifiedByGoogle': verifiedByGoogle,
        'VerifiedBusiness': verifiedBusiness,
        'VerifiedPaymentMethod': verifiedPaymentMethod,
        'HasCollectedIncentivizedReviews': hasCollectedIncentivisedReviews,
        'Email': email,
        'Address': address,
        'City': city,
        'Country': country,
        'PhoneNumber': phone,
        'ZIPCode': zipCode,
        'IsUsingPaidFeatures': isUsingPaidFeatures,
        'HasSubscription': hasSubscription,
        'IsAskingForReviews': isAskingForReviews,
        'ClaimedDate': claimedDate,
        'AverageDaystoReply': averageDaysToReply,
        'LastReplyToNegativeReview': lastReplyToNegativeReview,
        'NegativeReviewsWithReplies': negativeReviewsWithRepliesCount,
        'ReplyPercentage': replyPercentage,
        'TotalNegativeReviews': totalNegativeReviewsCount,
        'Reviews': reviews,
        'NumberOfReviews': totalNumberOfReviews,
        'NumberOfFilteredReviews': totalNumberOfFilteredReviews,
        'CurrentPage': currentPage,
        'ReviewsPerPage': perPage,
        'TotalReviewCount': totalCount,
        'TotalPages': totalPages,
        'RatingsCount': ratingsTotal,
        'OneStarRatingsCount': ratingsOneStar,
        'TwoStarRatingsCount': ratingsTwoStar,
        'ThreeStarRatingsCount': ratingsThreeStar,
        'FourStarRatingsCount': ratingsFourStar,
        'FiveStarRatingsCount': ratingsFiveStar
    }
    
        # Dump the output to .json
    with open('page_info.json', 'w') as outfile:
        json.dump(page_info, outfile)


if __name__ == "__main__":
    main()









































