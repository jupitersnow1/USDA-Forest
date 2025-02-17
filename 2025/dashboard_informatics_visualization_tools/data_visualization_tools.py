# Description: This script contains the libraries that will be used for data visualization in the 2025 project.

# correlation matrix 
# pair plot 
# summary statistics
# geometries


import pickle # to read from pkl files
import pandas as pd

# for data manipulation
import geopandas as gpd 

# for data visualization 
import seaborn as sb
import matplotlib.pyplot as plt



class Visualizer:
    """
    A class for visualizing data and models with support for
    Pandas DataFrames and GeoPandas GeoDataFrames.
    """

    def __init__(self, model=None, data=None):
        """
        Initialize the Visualizer object with the data and model.
        
        Parameters:
        model (str): trained model (optional)
        data (DataFrame): A pandas DataFrame or GeoDataFrame (optional)
        """
        self.model = model
        self.data = data

    @staticmethod
    def load_model(file_path):
        """
        Load a model from a .pkl file.
        """
        with open(file_path, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def load_sample_data():
        """
        Load a sample dataset (if no data is provided).
        """
        return sb.load_dataset('iris')

    def set_data(self, data):
        """
        Set or update the dataset.
        """
        self.data = data

    def set_model(self, model):
        """
        Set or update the model.
        """
        self.model = model

    def show_corr_matrix(self):
        """
        Show the correlation matrix of the dataset.
        """
        if self.data is None or self.data.select_dtypes(include='number').empty:
            print("No numerical data available for correlation matrix.")
            return

        corr_matrix = self.data.corr()
        plt.figure(figsize=(10, 6))
        sb.heatmap(corr_matrix, annot=True)
        plt.title("Correlation Matrix")
        plt.show()

    def show_pair_plot(self):
        """
        Display a pair plot of the dataset.
        """
        if self.data is None or self.data.select_dtypes(include='number').empty:
            print("No numerical data available for pair plot.")
            return

        sb.pairplot(self.data)
        plt.title("Pair Plot")
        plt.show()

    def show_summary_stats(self):
        """
        Display the summary statistics of the dataset.
        """
        if self.data is None or self.data.select_dtypes(include='number').empty:
            print("No numerical data available for summary statistics.")
            return

        print("\nSummary statistics of the data:")
        print(self.data.describe())

    def plot_geometries(self):
        """
        Plot the geometries if the data is a GeoDataFrame.
        """
        if self.data is None or not isinstance(self.data, gpd.GeoDataFrame):
            print("No geospatial data available for plotting.")
            return

        print("Plotting the geometries...")
        self.data.plot()
        plt.title("Geometries in GeoDataFrame")
        plt.show()

    def interactive_menu(self):
        """ 
        An interactive menu for visualizing data and models.
        """

        while True:
            print("\nChoose a visualtion option:")
            print("1. Show Correlation Matrix")
            print("2. Show Pair Plot")
            print("3. Show Summary Statistics")
            if isinstance(self.data, gpd.GeoDataFrame):
                print("4. Plot Geometries")
            else:
                print("4. Load Sample Data")

            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.show_corr_matrix()
            elif choice == '2':
                self.show_pair_plot()
            elif choice == '3':
                self.show_summary_stats()
            elif choice == '4':
                if isinstance(self.data, gpd.GeoDataFrame):
                    self.plot_geometries()
                else:
                    self.set_data(self.load_sample_data())
            elif choice == '5':
                print("Exiting the visualizer...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

#
# # import the class from the script
# from visualization_tool import Visualizer
# import seaborn as sb

# # Create a Visualizer object with sample data
# visualizer = Visualizer(data=sb.load_dataset('iris'))

# # optionally, you can show various visualizations:
# visualizer.show_corr_matrix()  # show the correlation matrix
# visualizer.show_pair_plot()    # show the pair plot
# visualizer.show_summary_stats() # show summary statistics

# # if you have geospatial data (GeoDataFrame), you can plot geometries:
# # visualizer.plot_geometries()

# # alternatively, invoke the interactive menu
# visualizer.interactive_menu()
