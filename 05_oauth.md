# OAuth

**Pages**
| Previous | Home | Next |
|---|---|---|
| [Object Oriented Programming](https://github.com/rysharprules/Rython/blob/master/04_oop.md) | [Home](https://github.com/rysharprules/Rython) | [Testing](https://github.com/rysharprules/Rython/blob/master/06_testing.md) |

----

**Contents**
- [OAuth](#oauth)
  - [OAuth Overview](#oauth-overview)
    - [How it works](#how-it-works)
      - [Code vs Access Token](#code-vs-access-token)
  - [Example OAuth Github application](#example-oauth-github-application)
    - [`oauthlib.oauth2`](#oauthliboauth2)
    - [Redirect to provider on user login](#redirect-to-provider-on-user-login)
    - [Handle the callback](#handle-the-callback)

## OAuth Overview

By using OAuth, a site can authenticate a user by just asking a 'provider' to do the authentication for it. This is great for the site, as it doesn't have to worry about doing authentication itself, and great for the user as they only need to remember their account details for a single 'provider' - not all of the individual sites.

### How it works

Note: There are 2 major versions, OAuth 1.0 and OAuth 2.0. We will be working with version 2 as its a little simpler to implement and more widely used.

- Step 1 - **Register your App** - The details vary between providers, but they will all require you to register your app with them. Once registered, your app will be issued with a _Client ID_ and a _Client Secret_. The ID can be public, but as the name suggest the secret should be kept secure. The combination of ID and Secret will be used later to authenticate the application (similar to a username and password).
- Step 2 - **Redirect users to your provider** - Once you've registered with a provider, you can add that provider as a sign in option on your site. When a user selects this sign in option, your app should add some information about what your app is and what permissions it would like to have, and then redirects the user to the provider's site. The permissions your app asks for is called the 'scope'. On the provider's site, the user will sign in, and then grant consent for your app to have that scope. 
- Step 3 - **Parse the Provider's response** - Once the user has signed in and granted consent, the provider will send a message to your application containing a 'code'. This works by your app providing a 'callback' endpoint which is called by the provider.
- Step 4 - **Get an access token** - Your app can then make a new request to the provider to exchange this code for an 'access token'.
- Step 5 - **Use the API** - Now we've got the access key, we can use it to make requests to the API. Note that the access key will only provide access to information / actions that are defined in the scope that we requested back in step 2.

#### Code vs Access Token

What's the difference between that 'code' and the 'access token'? After all, they are just strings, and the code is only used to collect the access token... why couldn't the provider just return the access token straight away? 

The reason is security. In order to be sure that it safe to issue an access token the provider needs 3 things:

1. Confirmation that the user is who they claim to be
1. Confirmation that the user is happy to provide access to the scope
1. Confirmation that the application is what it claims to be
   
When the provider issues the 'code', it only has the first 2 confirmations. It is confident about who the user is and what the user wants, but it isn't yet sure that the application is what it claims to be. So instead of issuing an access key, it instead issues a code. The application can then make a separate request, including the 'code', the 'Client ID' and the 'Client Secret'. The code provides confirmation for the first 2 points, and the ID + Secret authenticate the application. The provider can now be sure that it is safe to issue the access key.

## Example OAuth Github application

See the full example project, [OAuth Fiat Cinquecento](https://github.com/rysharprules/python-oauth-example/tree/exercise).

For Step 1 cited above, Github provides a simple [Creating an OAuth App](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/) guide performed on their site. Details on their endpoints are detailed on their [Authoring OAuth Apps](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/) guide.

### `oauthlib.oauth2`

We use the `oauthlib.oauth2` library ([documentation here](https://oauthlib.readthedocs.io/en/latest/oauth2/clients/baseclient.html)) to create and read the requests and responses between our application and our provider (Github).

`from oauthlib.oauth2 import WebApplicationClient`

We create our `WebApplicationClient` class and initialise it with the `CLIENT_ID`: `client = WebApplicationClient(CLIENT_ID)`.

### Redirect to provider on user login

We use the Flask `redirect` method to redirect the user to our provider's login URI. We use the `prepare_request_uri` helper method to give us default params, e.g. for `scope` and `CLIENT_ID` (set when initialising the `client` object).

````
@app.route('/login')
def login():
    return redirect(client.prepare_request_uri('https://github.com/login/oauth/authorize'))
````

### Handle the callback

We have a callback route which we set up with our provider when registering the application. Once the user logs in, the provider will call our callback route with a `code` argument:

````
@app.route('/login/callback')
def callback():
    code = request.args.get('code')
````

We can use the `code` to call our provider again to retrieve the access token:

````
 token_url, headers, body = client.prepare_token_request('https://github.com/login/oauth/access_token', code=code)
    headers['Accept'] = 'application/json'
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(CLIENT_ID, CLIENT_SECRET),
    )
````

Again we use a helper method from `WebApplicationClient`, `prepare_token_request`, to build our request object. Note, to get JSON back we need to add to the header an "Accept" header for "application/json". Also note we are sending our `CLIENT_SECRET` to to the provider on this call.

We can then parse the response with the `parse_request_body_response` helper method. We also the `json` library to serialise the JSON object with [json.dumps](https://docs.python.org/3/library/json.html#json.dump):

`client.parse_request_body_response(json.dumps(token_response.json()))`

Now the access token is within our `client`, we can construct the request to our provider's API (in this case Github's user API) and retrieve data on the signed in user:

````
uri, headers, body = client.add_token('https://api.github.com/user')
user_response = requests.get(uri, headers=headers).json()
````

We can print this to see all the available details in this object:

`print(user_response, file=sys.stdout) # Note the file attribute is required for console output when using Flask`