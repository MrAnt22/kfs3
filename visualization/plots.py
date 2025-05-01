import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_air_quality(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    plt.plot(df['datetime'], df['air_quality_index'], label='Індекс якості повітря', color='blue')
    plt.xlabel('Дата')
    plt.ylabel('Індекс якості повітря (AQI)')
    plt.title('Динаміка якості повітря з часом')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_weather_trends(df: pd.DataFrame):
    plt.figure(figsize=(14, 8))

    plt.subplot(3, 1, 1)
    plt.plot(df['datetime'], df['temperature'], label='Температура (°C)', color='red')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(df['datetime'], df['humidity'], label='Вологість (%)', color='blue')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(df['datetime'], df['wind_speed'], label='Швидкість вітру (м/с)', color='purple')
    plt.legend()
    plt.grid(True)

    plt.xlabel('Дата')
    plt.suptitle('Тренди погоди')
    plt.tight_layout()
    plt.show()

def plot_air_quality_for_allergies(df, return_fig=False):
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.scatterplot(data=df, x='datetime', y='air_quality_index', hue='air_quality_category', palette='deep', s=100, ax=ax)
    
    ax.set_title('Якість повітря з рекомендаціями для алергіків')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Індекс якості повітря (AQI)')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.grid(True)
    fig.tight_layout()

    if return_fig:
        return fig
    else:
        plt.show()