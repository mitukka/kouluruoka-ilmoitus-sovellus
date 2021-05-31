package me.mitja.kouluruokailmo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {

    Button testBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        testBtn = (Button)findViewById(R.id.testBtn);

        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform((this)));
    }
        Python py = Python.getInstance();
        final PyObject pyobj = py.getModule("script");

        testBtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                PyObject data = pyobj.callAttr("request");

                Toast.makeText(getApplicationContext(), data.toString(), Toast.LENGTH_LONG).show();
            }
        });
    }
}