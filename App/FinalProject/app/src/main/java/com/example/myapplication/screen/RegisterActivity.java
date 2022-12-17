package com.example.myapplication.screen;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.app.Activity;
import android.graphics.Bitmap;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import com.example.myapplication.service.ConvertToString;
import com.example.myapplication.R;
import com.example.myapplication.service.ApiService;
import com.example.myapplication.model.User;

import java.io.IOException;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
public class RegisterActivity extends AppCompatActivity {
    Button buttonCapture,buttonRecognition,buttonSelect;
    ImageView imageAva;
    EditText textEnterName;
    Bitmap imageBitmap;
    String stringImage;
    private static final int REQUESTCODE =10 ;
    private static final String TAG = MainActivity.class.getName();
    private static final int REQUEST_ID_IMAGE_CAPTURE = 100;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_capture);
        Init();
        CaptureImage();
        recognitionCLick();
        selectRegister();
    }
    void Init(){
        buttonCapture=findViewById(R.id.buttonCap);
        imageAva=findViewById(R.id.imageViewAva);
        textEnterName=findViewById(R.id.editTextName);
        buttonRecognition=findViewById(R.id.buttonrecognition);
        buttonSelect=findViewById(R.id.buttonSelectRegis);

    }
    void selectRegister(){
        buttonSelect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                onClickRequestPermission();
            }
        });
    }
    void recognitionCLick(){
        buttonRecognition.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                User userRequest=new User(stringImage,textEnterName.getText().toString());
                ApiService.apiService.requestRegisterUser(userRequest).enqueue(new Callback<User>() {
                    @Override
                    public void onResponse(Call<User> call, Response<User> response) {
                        User useResult=response.body();
                        if(useResult!=null) {
                            Toast.makeText(RegisterActivity.this, "Register Success", Toast.LENGTH_LONG).show();
                            Intent intent = new Intent(RegisterActivity.this, HomeActivity.class);
                            intent.putExtra("userName", textEnterName.getText().toString());
                            startActivity(intent);
                        }
                        else
                        {
                            Toast.makeText(RegisterActivity.this, "ERROR API!!", Toast.LENGTH_LONG).show();
                        }
                    }
                    @Override
                    public void onFailure(Call<User> call, Throwable t) {
                        Toast.makeText(RegisterActivity.this,"Register Fail",Toast.LENGTH_LONG).show();

                    }
                });
            }
        });
    }
    private ActivityResultLauncher<Intent> mActivivityResultLauncher=registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            new ActivityResultCallback<ActivityResult>() {
                @Override
                public void onActivityResult(ActivityResult result) {
                    Log.e(TAG,"onActivityResult*");
                    if (result.getResultCode()== Activity.RESULT_OK)
                    {
                        Intent data=result.getData();
                        if (data==null)
                        {
                            return;
                        }
                        Uri uri=data.getData();
                        try {
                            Bitmap bitmap= MediaStore.Images.Media.getBitmap(getContentResolver(),uri);
                            imageAva.setImageBitmap(bitmap);
                            stringImage= ConvertToString.ConvertToString(bitmap);
                        }
                        catch (IOException e)
                        {
                            e.printStackTrace();
                        }
                    }
                }
            });

    void CaptureImage(){
        this.buttonCapture.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                captureImage();
            }
        });
    }
    private void OpenGallery() {
        Intent intent=new Intent();
        intent.setType("image/*");
        intent.setAction(intent.ACTION_GET_CONTENT);
        mActivivityResultLauncher.launch(Intent.createChooser(intent,"Choose Picture"));
    }
    private void onClickRequestPermission() {
        if (Build.VERSION.SDK_INT< Build.VERSION_CODES.M)
        {
            OpenGallery();
            return;
        }
        if (ActivityCompat.checkSelfPermission(getApplicationContext(),
                Manifest.permission.READ_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED)
        {
            OpenGallery();
        }
        else {
            String[]permission={Manifest.permission.READ_EXTERNAL_STORAGE};
            requestPermissions(permission,REQUESTCODE);
        }
    }
    private void captureImage() {
        // Create an implicit intent, for image capture.
        Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);

        // Start camera and wait for the results.
        this.startActivityForResult(intent, REQUEST_ID_IMAGE_CAPTURE);
    }
    // When results returned
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == REQUEST_ID_IMAGE_CAPTURE) {
            if (resultCode == RESULT_OK) {
                // data dau ra
                imageBitmap = (Bitmap) data.getExtras().get("data");
                this.imageAva.setImageBitmap(imageBitmap);
                stringImage=ConvertToString.ConvertToString(imageBitmap);
            } else if (resultCode == RESULT_CANCELED) {
                Toast.makeText(this, "Action canceled", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(this, "Action Failed", Toast.LENGTH_LONG).show();
            }
        }
    }



}

