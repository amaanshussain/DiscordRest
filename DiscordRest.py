import requests

class DiscordRest:

    def __init__(self, token):

        self.token = token

        self.headers = {"Authorization": f"Bot {token}"}

        self.BASE_URL = "https://discord.com/api"
    
    def _get(self, endpoint, params = None, headers = None):

        response = requests.get(self.BASE_URL + endpoint, params = params, headers = headers)

        return response

    def _post(self, endpoint, params = None, json = None, headers = None):

        response = requests.post(self.BASE_URL + endpoint, params = params, json = json, headers = headers)

        return response

    def _put(self, endpoint, params = None, headers = None):

        response = requests.put(self.BASE_URL + endpoint, params = params, headers = headers)

        return response

    def _patch(self, endpoint, params = None, json = None, headers = None):

        response = requests.patch(self.BASE_URL + endpoint, params = params, json = json, headers = headers)

        return response
    
    def _delete(self, endpoint, params = None, headers = None):

        response = requests.delete(self.BASE_URL + endpoint, params = params, headers = headers)

        return response

    # Audit
    def audit_log(self, guild_id: int, user_id: int = None, action_type: int = None, before: int = None, limit: int = None) -> dict:
        """
        Requires the 'VIEW_AUDIT_LOG' permission.

        """

        params = {}
        if user_id != None:
            params["user_id"] = user_id
        if action_type != None:
            params["action_type"] = action_type
        if before != None:
            params["before"] = before
        if limit != None:
            params["limit"] = limit


        response = self._get(f"/guilds/{guild_id}/audit-logs", params = params, headers = self.headers)

        return response.json()

    # Channels
    def get_channel(self, channel_id: int) -> dict:
        """
        Gets channel object by id.

        """

        response = self._get(f"/channels/{channel_id}", headers = self.headers)

        return response.json()

    def modify_channel(self, channel_id: int, name: str = None, type: int = None, position: int = None, topic: str = None, nsfw: bool = None, slow_mode: int = None, bitrate: int = None, user_limit: int = None, category_id: int = None) -> dict:
        """
        Requires the 'MANAGE_CHANNELS' permission for the guild. 

        """

        json = {}
        if name != None:
            json["name"] = name
        if type != None:
            json["type"] = type
        if position != None:
            json["position"] = position
        if topic != None:
            json["topic"] = topic
        if nsfw != None:
            json["nsfw"] = nsfw
        if slow_mode != None:
            json["rate_limit_per_user"] = slow_mode
        if bitrate != None:
            json["bitrate"] = bitrate
        if user_limit != None:
            json["user_limit"] = user_limit
        if category_id != None:
            json["parent_id"] = category_id


        response = self._patch(f"/channels/{channel_id}", json = json, headers = self.headers)

        return response.json()

    def delete_channel(self, channel_id: int) -> dict:
        """
        Requires the 'MANAGE_CHANNELS' permission for the guild.

        """
        response = self._delete(f"/channels/{channel_id}", headers = self.headers)

        return response.json()

    def get_messages(self, channel_id: int, around: int = None, before: int = None, after: int = None, limit: int = None) -> dict:
        """
        Requires the 'VIEW_CHANNEL' permission for the guild.

        The before, after, and around keys are mutually exclusive, only one may be passed at a time.

        """

        params = {}
        if around != None:
            params["around"] = around
        if before != None:
            params["before"] = before
        if after != None:
            params["after"] = after
        if limit != None:
            params["limit"] = limit

        response = self._get(f"/channels/{channel_id}/messages", headers = self.headers)

        return response.json()

    def get_message(self, channel_id: int, message_id: int) -> dict:
        """
        Requires the 'READ_MESSAGE_HISTORY' permission for the guild.

        """

        response = self._get(f"/channels/{channel_id}/messages/{message_id}", headers = self.headers)

        return response.json()


    # Emoji
    def get_emojis(self, guild_id: int) -> dict:
        """
        Retrives list of emojis from server.
        """

        response = self._get(f"/guilds/{guild_id}/emojis", headers = self.headers)

        return response.json()

    def get_emoji(self, guild_id: int, emoji_id: int) -> dict:
        """
        Returns emoji object of supplied id.
        """

        response = self._get(f"/guilds/{guild_id}/emojis/{emoji_id}", headers = self.headers)

        return response.json()

    def create_emoji(self, guild_id: int, name: str = None, image: str = None) -> dict:
        """
        Creates emoji in given server.

        Supply image as Data URI Scheme (jpeg, png, gif):
        data:image/jpeg;base64,BASE64_ENCODED_JPEG_IMAGE_DATA
        """

        json = {}
        if name != None:
            json["name"] = name
        if image != None:
            json["image"] = image
        
        response = self._post(f"/guilds/{guild_id}/emojis", json = json, headers = self.headers)

        return response.json()

    def modify_emoji(self, guild_id: int, emoji_id: int, name: str = None) -> dict:
        """
        Requires the 'MANAGE_EMOJIS_AND_STICKERS' permission

        """

        json = {}
        if name != None:
            json["name"] = name

        response = self._patch(f"/guilds/{guild_id}/emojis/{emoji_id}", json = json, headers = self.headers)

        return response.json()

    def delete_emoji(self, guild_id: int, emoji_id: int) -> dict:
        """
        Requires the 'MANAGE_EMOJIS_AND_STICKERS' permission

        """

        response = self._delete(f"/guilds/{guild_id}/emojis/{emoji_id}", headers = self.headers)

        return response.json()


    # User
    def get_user(self, user_id) -> dict:
        """
        Retrieves user object given id.
        """

        response = self._get(f"/users/{user_id}", headers = self.headers)

        return response.json()

    def modify_user(self, username: str = None, avatar: str = None) -> dict:
        """
        Modifies user account of self.
        """

        json = {}
        if username != None:
            json["username"] = username
        if avatar != None:
            json["avatar"] = avatar

        response = self._patch("/users/@me", json = json, headers = self.headers)

        return response.json()
    
    def get_self_guilds(self, limit: int = None) -> dict:
        """
        Gets list of all users guilds.
        """

        params = {}
        if limit != None:
            params["limit"] = limit
        
        response = self._get("/users/@me/guilds", params = params, headers = self.headers)

        return response.json()
    
    def leave_guild(self, guild_id: int) -> dict:
        """
        Leaves specified guild.
        """

        response = self._delete(f"/users/@me/guilds/{guild_id}", headers = self.headers)

        return response.json()
    