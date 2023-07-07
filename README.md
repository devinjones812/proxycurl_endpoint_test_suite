# About

This package contains a full test suite for the **Proxycurl** APIs and their endpoints. Under each API subdirectory, you will find its corresponding endpoints. Each endpoint file has an example taken directly from the Proxycurl docs and is easy to experiment with to determine whether it will match your needs.

# Getting Started

In order to run these examples, you will need to create a **.env** file in the project's home directory and store your Proxycurl API key in it, like this:  `PROXYCURL_API_KEY=your_api_key` 

## Tips

You can check the number of credits you have remaining by running the **view_credit_balance** endpoint located in the **meta_api** subdirectory.

I've also left comments at the top and bottom of some endpoints that seem to fail to return the right result, take too many credits, or do anything that seems to be abnormal.