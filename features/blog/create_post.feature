Feature: create post

Scenario: Successful creating a post 

When I go to "http://localhost:3000/posts"
Then I click on the link "New Post"
Then I fill "Tom is a boy" in the field with the label "Title"
Then I fill "QQQQQQQQQQQQQQQ" in the field with the label "Body"
When I press the button "Create Post" 
Then the page has "Post was successfully created."

Scenario: Editing a post 

When I go to "http://localhost:3000/posts"
Then I click on the last link with the text "Edit"
Then I fill "Nona is a girl" in the field with the label "Title"
Then I fill "1234567890" in the field with the label "Body"
When I press the button "Update Post"
Then the page has "Post was successfully updated."
Then the page has "Nona is a girl"
Then the page has "1234567890"

Scenario: Deleting a post

Then I click on the link "Back"
Then I click on the last link with the text "Destroy"
Then I accept alert
Then I wait for "1"
Then the page has "Post was successfully destroyed."
Then the page does not have "1234567890"
Then the page does not have "Nona is a girl"

Scenario: The post should not be created if required fields are not filled

When I go to "http://localhost:3000/posts"
Then I click on the link "New Post"
When I press the button "Create Post"
Then the page does not have "Post was successfully created."
Then the page has "2 errors prohibited this post from being saved:"
Then the page has "Body can't be blank"
Then the page has "Title can't be blank"




#Post was successfully destroyed.