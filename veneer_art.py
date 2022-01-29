# Add a wallet instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
# Create a wishlist for your clients, things that are listed but they’re not sure if they should purchase just yet.
# Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.

class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{a}. \"{t}\". {y}, {m}. {o}, {l}.".format(o=self.owner.name, l=self.owner.location, a=self.artist,
                                                          t=self.title, y=self.year, m=self.medium)


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, old_listing):
        self.listings.remove(old_listing)

    def show_listings(self):
        print("Current Listing")
        for item in self.listings:
            print(item)


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if artwork == listing.art:
                    art_listing = listing
                    break
            if art_listing != None:
                artwork.owner = self
                veneer.remove_listing(art_listing)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{art}, £{price}".format(art=self.art.title, price=self.price)


veneer = Marketplace()

edytta = Client("Edytta Halpirt", None, False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
in_the_fog = Art("Picasso, Pablo", "Vetheuil in the Fog", "oil on canvas", 1879, moma)

edytta.sell_artwork(girl_with_mandolin, "6M")
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()
