package tcs.lbs.intentsniffer;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.location.Location;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity
{
    TextView LatitudeTextView, LongitudeTextView;

    static final String Inter_RECEIVER_ACTION = "tcs.lbs.weather_app.WeatherBroadcastReceiver";
    static final String Intra_RECEIVER_ACTION = "tcs.lbs.locationapp.MainActivityReceiver";
    SnifferBroadcastReceiver lReceiver;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        LatitudeTextView = findViewById(R.id.LatitudeTextView);
        LongitudeTextView = findViewById(R.id.LongitudeTextView);
    }

    @Override
    protected void onResume()
    {
        super.onResume();

        IntentFilter filter = new IntentFilter();
        filter.addAction("tcs.lbs.weather_app.WeatherBroadcastReceiver");
        filter.addAction("tcs.lbs.locationapp.MainActivityReceiver");

        lReceiver = new SnifferBroadcastReceiver();
        registerReceiver(lReceiver, filter);
    }

    public class SnifferBroadcastReceiver extends BroadcastReceiver
    {
        @SuppressLint("SetTextI18n")
        @Override
        public void onReceive(Context context, Intent intent)
        {
            Bundle extras = intent.getExtras();
            Location location = (Location)extras.get("Location");
            if (location != null){
                LatitudeTextView.setText(location.getLatitude() + "");
                LongitudeTextView.setText(location.getLongitude() + "");
            }
        }
    }
}
