# Shorten URL

Shorten URL is a URL shortening service similar to TinyURL, designed to
transform long URLs into short, easy-to-share links.

## Application Configuration

Configuration of the application is managed by passing a callback 
function to the factory method. While Flask offers multiple options for 
[configuration handling][3], it's ultimately up to you to determine the 
most suitable approach for your needs.

Sensitive information, such as API keys or database credentials, should 
generally not be included in version control systems like Git. Therefore, 
an example configuration file is not provided here. See below for any 
configurations expected by the application.

Currently, no configurations are required.

## Acknowledgements 

Many thanks to the creators and maintainers at [Coding Challenges][1]
for providing the idea and foundational concepts for building a URL
shortening service through the [URL Shortener Challenge][2].

[1]: https://codingchallenges.fyi/
[2]: https://codingchallenges.fyi/challenges/challenge-url-shortener
[3]: https://flask.palletsprojects.com/en/stable/config/
