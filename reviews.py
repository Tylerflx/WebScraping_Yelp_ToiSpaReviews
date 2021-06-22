def scrape_review(lists):
    #cant call ul because the whole page using the same methods and attributes
    for each in lists:
        reviewer_name = each.find('span', class_='fs-block css-m6anxm').a.text
        reviewer_location = each.find('span', class_='css-n6i4z7').text
        rating = each.find('div', class_='i-stars__373c0__1T6rz')
        star_rating = rating['aria-label']
        #can do if statement to create an average rating feature
        review_date = each.find('span', class_='css-e81eai').text
        review = each.find('span', class_='raw__373c0__3rcx7').text
        print('')
        print(reviewer_name)
        print(reviewer_location)
        print(star_rating)
        print(review_date)
        print(review)
        print('_____________________%____________________')