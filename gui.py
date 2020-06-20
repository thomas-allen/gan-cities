import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import gancities


class GanCities(Gtk.Window):
    def __init__(self):
        super(GanCities, self).__init__()
        self.generator = gancities.CityGenerator()
        self.countries = self.generator.getValidCountries()
        self.pixbuf = GdkPixbuf.Pixbuf.new_from_file("gui_placeholder_images/sample.png")
        self.initialize_ui()
        self.load_image()

    def initialize_ui(self):
        # Layout
        self.horiz_box = Gtk.Box()
        self.resize(600,400)
        self.options_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.image_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.horiz_box.pack_start(self.options_box, False, True, 10)
        self.horiz_box.pack_start(self.image_box, True, True, 10)
        self.set_title("GanCities")
        self.connect("check_resize", self.on_check_resize)
        self.connect("delete-event", Gtk.main_quit)
        # Image Display
        self.image_area = Gtk.DrawingArea()
        self.image_area.connect("draw", self.on_draw)
        self.image_box.pack_start(self.image_area, True, True, 10)
        # Training Selection
        self.train_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.train_label = Gtk.Label(label="Training Folder:")
        self.train_folder_select = Gtk.FileChooserButton(title="Training Folder", action=Gtk.FileChooserAction.SELECT_FOLDER)
        self.train_button = Gtk.Button(label="Start Training")
        self.train_button.connect("clicked", self.train_clicked, self.generator, self.train_folder_select)
        self.train_box.pack_start(self.train_label, False, True, 10)
        self.train_box.pack_start(self.train_folder_select, False, False, 10)
        self.train_box.pack_start(self.train_button,True, True, 10)
        # Country Style Combobox
        self.country_model = Gtk.ListStore(str)
        for country in self.generator.getValidCountries():
            print([country])
            self.country_model.append([country])
        self.country_style=Gtk.ComboBox(model=self.country_model)
        cell = Gtk.CellRendererText()
        self.country_style.pack_start(cell, False)
        self.country_style.add_attribute(cell, "text", 0)
        self.country_style.set_entry_text_column(0)
        self.country_style.set_active(0)
        # Population Spin Button
        pop_adjustment = Gtk.Adjustment(value=1000, lower=1000, upper=10000000, step_increment=1000)
        self.popspinner = Gtk.SpinButton(numeric=True)
        self.popspinner.set_adjustment(pop_adjustment)
        # Dimensions
        self.dim_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.dimlabel1 = Gtk.Label(label="Map Dimensions")
        self.dimlabel2 = Gtk.Label(label="x")
        dim_xadjustment = Gtk.Adjustment(value=400, lower=200, upper=3440, step_increment=10)
        dim_yadjustment = Gtk.Adjustment(value=400, lower=200, upper=3440, step_increment=10)
        self.xspinner = Gtk.SpinButton(numeric=True, adjustment=dim_xadjustment)
        self.yspinner = Gtk.SpinButton(numeric=True, adjustment=dim_yadjustment)
        self.dim_box.pack_start(self.dimlabel1, True, True, 0)
        self.dim_box.pack_start(self.xspinner, True, True, 0)
        self.dim_box.pack_start(self.dimlabel2, True, True, 0)
        self.dim_box.pack_start(self.yspinner, True, True, 0)
        # Make Map button
        self.button = Gtk.Button(label="Make a map")
        self.button.connect("clicked", self.on_button_clicked)
        # Packing
        self.options_box.pack_start(self.train_box, True, True, 10)
        self.options_box.pack_start(self.country_style, False, False, 10)
        self.options_box.pack_start(self.popspinner, True, True, 10)
        self.options_box.pack_start(self.dim_box, True, True, 10)
        self.options_box.pack_start(self.button, True, True, 10)
        self.add(self.horiz_box)
        self.show_all()

    def on_check_resize(self, window):
        allocation = self.image_area.get_allocation()
        self.image_area.set_allocation(allocation)
        self.resizeImage(allocation.width, allocation.height)

    def load_image(self):
        self.scale_pixbuf = self.pixbuf.scale_simple(400, 400, GdkPixbuf.InterpType.BILINEAR)

    def resizeImage(self, x, y):
        self.scale_pixbuf = self.pixbuf.scale_simple(x, y, GdkPixbuf.InterpType.BILINEAR)

    def on_draw(self, win, cr):
        Gdk.cairo_set_source_pixbuf(cr, self.scale_pixbuf, 5, 5)
        cr.paint()

    def on_button_clicked(self, widget):
        print("Making a " + str(self.countries[self.country_style.get_active()]) + " style map.")
        print("This map will have " + str(self.popspinner.get_value()) + " set as the population.")
        print("This map will be " + str(self.xspinner.get_value()) + "x" + str(self.yspinner.get_value()))

    def train_clicked(self, widget, generator, chooser):
        if chooser.get_file() is not None:
            generator.train(chooser.get_file().get_uri())
def main():
    application = GanCities()
    Gtk.main()


if __name__ == "__main__":
    main()
