Feature: testing python.org

Scenario: visit python.org and check title

When I visit https://www.python.org/
  Then it should have a title "Python"
When I search "hello" in the field with name "q"
  Then page should have content "Hello"